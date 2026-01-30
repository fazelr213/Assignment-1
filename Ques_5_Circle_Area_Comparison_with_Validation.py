
import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    if not isinstance(radiusOfCircle1, int) or not isinstance(radiusOfCircle2, int) or radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "radius is not a postive integer"

    area_of_circle1 = math.pi * radiusOfCircle1 * radiusOfCircle1

    area_of_circle2 = math.pi * radiusOfCircle2 * radiusOfCircle2

    return (min(area_of_circle1, area_of_circle2) / max(area_of_circle1, area_of_circle2)) * 100

print(circleAreaCoverage(1, 2))


