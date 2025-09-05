from imgRecon import recon
from display import output_display

slots = [[[152, 119], [382, 123], [292, 448], [23, 445]], 
        [[472, 121], [704, 122], [678, 449], [401, 447]], 
        [[793, 121], [1019, 118], [1063, 445], [790, 444]], 
        [[1115, 116], [1345, 113], [1457, 444], [1178, 443]]]

imgPath = r"./Images/test.jpeg"

if __name__ == "__main__":
    availSlots = recon(imgPath, slots)
    output_display(availSlots)