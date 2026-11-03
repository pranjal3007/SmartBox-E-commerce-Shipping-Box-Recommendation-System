
from itertools import product, permutations


def calculate_volume(length, width, height):
    return length * width * height


def check_overlap(position, dimensions, placed_item):
    x, y, z = position
    length, width, height = dimensions

    px, py, pz = placed_item["position"]
    pl, pw, ph = placed_item["dimensions"]

    overlap_x = x < px + pl and x + length > px
    overlap_y = y < py + pw and y + width > py
    overlap_z = z < pz + ph and z + height > pz

    return overlap_x and overlap_y and overlap_z


def pack_products(products, box):
    """
    Try to pack all products into one box.
    Rotation is allowed. Products cannot be split.
    Returns placement details or None if packing fails.
    """

    box_length = box["length"]
    box_width = box["width"]
    box_height = box["height"]

    products = sorted(
        products,
        key=lambda item: calculate_volume(
            item["length"],
            item["width"],
            item["height"]
        ),
        reverse=True
    )

    placed_items = []

    for item in products:
        original_dimensions = (
            item["length"],
            item["width"],
            item["height"]
        )

        # Generate all unique orientations (up to 6).
        orientations = tuple(permutations(original_dimensions))

        # Generate possible placement coordinates.
        x_positions = {0}
        y_positions = {0}
        z_positions = {0}

        for placed in placed_items:
            px, py, pz = placed["position"]
            pl, pw, ph = placed["dimensions"]

            x_positions.add(px + pl)
            y_positions.add(py + pw)
            z_positions.add(pz + ph)

        positions = sorted(
            product(x_positions, y_positions, z_positions),
            key=lambda pos: (pos[2], pos[1], pos[0])
        )

        found_position = False

        for position in positions:
            x, y, z = position

            for dimensions in orientations:
                length, width, height = dimensions

                if (
                    x + length > box_length
                    or y + width > box_width
                    or z + height > box_height
                ):
                    continue

                collision = any(
                    check_overlap(position, dimensions, placed)
                    for placed in placed_items
                )

                if not collision:
                    placed_items.append({
                        "name": item["name"],
                        "position": position,
                        "dimensions": dimensions
                    })

                    found_position = True
                    break

            if found_position:
                break

        if not found_position:
            return None

    return placed_items


def recommend_box(order_products, available_boxes):
    """
    Recommend the cheapest suitable box for an entire order.

    Rotation is allowed.
    Multiple products can share one box.
    Orders cannot be split across boxes.
    Packaging padding is ignored.
    """

    if not order_products:
        return {
            "success": False,
            "message": "Order contains no products.",
            "rejected_boxes": []
        }

    if not available_boxes:
        return {
            "success": False,
            "message": "No shipping boxes are available.",
            "rejected_boxes": []
        }

    # Calculate total weight and number of physical products.
    total_weight = sum(
        item["weight"] * item["quantity"]
        for item in order_products
    )

    total_product_count = sum(
        item["quantity"]
        for item in order_products
    )

    # Expand quantities into individual products.
    individual_products = []

    for item in order_products:
        for _ in range(item["quantity"]):
            individual_products.append({
                "name": item["name"],
                "length": item["length"],
                "width": item["width"],
                "height": item["height"]
            })

    # Sort boxes by cost, then by volume.
    sorted_boxes = sorted(
        available_boxes,
        key=lambda box: (
            box["cost"],
            calculate_volume(
                box["length"],
                box["width"],
                box["height"]
            )
        )
    )

    rejected_boxes = []

    for box in sorted_boxes:

        box_volume = calculate_volume(
            box["length"],
            box["width"],
            box["height"]
        )

        # Check weight capacity.
        if total_weight > box["max_weight"]:
            rejected_boxes.append({
                "box": box["name"],
                "reason": "Order exceeds maximum weight capacity.",
                "max_weight": box["max_weight"],
                "order_weight": total_weight
            })
            continue

        # Check physical packing.
        placements = pack_products(
            individual_products,
            box
        )

        if placements is not None:

            return {
                "success": True,
                "message": "Suitable shipping box found.",

                "recommended_box": {
                    "name": box["name"],
                    "dimensions": {
                        "length": box["length"],
                        "width": box["width"],
                        "height": box["height"]
                    },
                    "max_weight": box["max_weight"],
                    "cost": box["cost"],
                    "volume": box_volume
                },

                "order_summary": {
                    "total_weight": total_weight,
                    "total_products": total_product_count
                },

                "placements": placements,

                "rejected_boxes": rejected_boxes
            }

        rejected_boxes.append({
            "box": box["name"],
            "reason": "Products could not be physically packed."
        })

    return {
        "success": False,
        "message": "No suitable box found for this order.",

        "order_summary": {
            "total_weight": total_weight,
            "total_products": total_product_count
        },

        "rejected_boxes": rejected_boxes
    }
