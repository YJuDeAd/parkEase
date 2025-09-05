import cv2
import numpy as np
from ultralytics import YOLO

def recon(path, slots):
    # Load model
    model = YOLO("yolov8x-seg.pt")

    results = model(path)
    img = cv2.imread(path)

    slot_status = [0] * len(slots)

    for r in results:
        if r.masks is not None:
            for mask in r.masks.data:
                mask = mask.cpu().numpy()
                mask = cv2.resize(mask, (img.shape[1], img.shape[0]))
                mask = (mask > 0.5).astype(np.uint8)

                # Find mask pixels
                ys, xs = np.where(mask == 1)
                points = np.vstack((xs, ys)).T

                # Check against each slot polygon
                for i, poly in enumerate(slots):
                    polygon = np.array(poly, np.int32)
                    for p in points[::50]:  # sample some points to speed up
                        if cv2.pointPolygonTest(polygon, (int(p[0]), int(p[1])), False) >= 0:
                            slot_status[i] = 1
                            break

    # Draw results
    for i, poly in enumerate(slots):
        color = (0, 255, 0) if slot_status[i] == 0 else (0, 0, 255)
        cv2.polylines(img, [np.array(poly, np.int32)], True, color, 3)
        textPosX = (((poly[0][0] + poly[1][0]) // 2) - 60)
        textPosY = poly[0][1] - 20
        textPos = (textPosX, textPosY)
        cv2.putText(img, f"Slot {i}:{slot_status[i]}",
                    textPos, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imwrite("./Images/output.png", img)
    print("✅ Saved as output.png")
    return slot_status