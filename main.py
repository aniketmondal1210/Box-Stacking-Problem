# main.py

class Box:
    def __init__(self, h, w, d):
        self.h = h
        self.w = w
        self.d = d

    def base_area(self):
        return self.w * self.d

    def __lt__(self, other):
        return self.base_area() < other.base_area()


def create_rotations(boxes):
    rotations = []
    for box in boxes:
        h, w, d = box.h, box.w, box.d
        rotations.append(Box(h, min(w, d), max(w, d)))
        rotations.append(Box(w, min(h, d), max(h, d)))
        rotations.append(Box(d, min(h, w), max(h, w)))
    return rotations


def max_stack_height(boxes):
    # Step 1: Create all 3 rotations of each box
    rotations = create_rotations(boxes)

    # Step 2: Sort the boxes in decreasing order of base area (width × depth)
    rotations.sort(reverse=True)

    n = len(rotations)
    msh = [0] * n  # msh[i] = max stack height ending with box i on top

    # Step 3: Initialize msh with height of each box
    for i in range(n):
        msh[i] = rotations[i].h

    # Step 4: Compute optimized msh values in bottom-up manner
    for i in range(1, n):
        for j in range(i):
            if (rotations[i].w < rotations[j].w and
                rotations[i].d < rotations[j].d):
                msh[i] = max(msh[i], msh[j] + rotations[i].h)

    # Step 5: Return the maximum value in msh[]
    return max(msh)


if __name__ == "__main__":
    # Input boxes: height, width, depth
    input_boxes = [
        Box(4, 6, 7),
        Box(1, 2, 3),
        Box(4, 5, 6),
        Box(10, 12, 32)
    ]
    result = max_stack_height(input_boxes)
    print("The maximum possible height of stack is", result)
