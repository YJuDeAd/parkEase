import numpy as np
import cv2


def output_display(slot_status):
    # Box settings
    box_size = 100   # width/height of each box
    margin = 20      # space between boxes

    # Create a blank black canvas
    width = len(slot_status) * (box_size + margin) + margin + 92
    height = box_size + 2 * margin + 238
    img = np.ones((height, width, 3), dtype=np.uint8) * 0  # black background

    # Draw boxes
    for i, status in enumerate(slot_status):
        x1 = margin + i * (box_size + margin) + 46
        y1 = margin + 119
        x2 = x1 + box_size
        y2 = y1 + box_size

        color = (0, 255, 0) if status == 0 else (0, 0, 255)  # green or red
        cv2.rectangle(img, (x1, y1), (x2, y2), color, -1)  # filled box
        if str(status) == '0':
            cv2.putText(img, "E", (x1 + 35, y1 + 65),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
        else:
            cv2.putText(img, "F", (x1 + 35, y1 + 65),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

    # Save output
    cv2.imwrite("./Images/available_slots.png", img)
    print("✅ Saved as slots_array.png")
