import numpy as np
import cv2

bounds = {
    "red": (np.array([160, 75, 75]), np.array([180, 255, 255])),
    "blue": (np.array([110, 75, 75]), np.array([130, 255, 255])),
    "green": (np.array([35, 75, 75]), np.array([85, 255, 255])),
    "yellow": (np.array([20, 75, 75]), np.array([40, 255, 255])),
    "white": (np.array([0, 0, 150]), np.array([180, 30, 255])),
    "orange": (np.array([10, 100, 100]), np.array([20, 255, 255]))
}

def density(img, color):
    lower = bounds[color][0]
    upper = bounds[color][1]
    mask = cv2.inRange(img, lower, upper)
    return np.sum(mask) / 255

def cubestr(data):
    ret = ""
    for i in "URFDLB":
        ret += "".join(data[i])
    for i in "URFDLB":
        ret = ret.replace(data[i][4], i)
    return ret

# Example usage
if __name__ == "__main__":
    # Example image (replace with your image)
    img = cv2.imread("example_image.jpg")
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Example usage of density function
    for color in bounds:
        dens = density(img_hsv, color)
        print(f"Density of {color}: {dens}")

    # Example usage of cubestr function
    data = {
        "U": ["w", "w", "w", "w", "w", "w", "w", "w", "w"],
        "R": ["r", "r", "r", "r", "r", "r", "r", "r", "r"],
        "F": ["b", "b", "b", "b", "b", "b", "b", "b", "b"],
        "D": ["y", "y", "y", "y", "y", "y", "y", "y", "y"],
        "L": ["o", "o", "o", "o", "o", "o", "o", "o", "o"],
        "B": ["g", "g", "g", "g", "g", "g", "g", "g", "g"]
    }
    cube_state = cubestr(data)
    print("Cube State:", cube_state)
