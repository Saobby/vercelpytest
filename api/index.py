from PIL import Image
from flask import *
import random
from io import *

app = Flask(__name__)


@app.route("/api/colorful_venti", methods=["get"])
def api_colorful_venti():
    color = request.args.get("color")
    if color is None:
        return "Args 'color' was missing", 400
    if color == "random":
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    else:
        rgb = color.split(",")
        if len(rgb) != 3:
            return "Invalid color", 400
        r, g, b = int(rgb[0]), int(rgb[1]), int(rgb[2])
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            return "Invalid color", 400
    green_part = Image.open("venti_green.png")
    origin = Image.open("venti_origin.png")
    for y in range(origin.size[1]):
        for x in range(origin.size[0]):
            nr, ng, nb, na = green_part.getpixel((x, y))
            gray = nr
            if gray != 255:
                gray_ = gray / 255
                ar, ag, ab = int(gray_*r*1.5), int(gray_*g*1.5), int(gray_*b*1.5)
                if ar > 255:
                    ar = 255
                if ag > 255:
                    ag = 255
                if ab > 255:
                    ab = 255
                origin.putpixel((x, y), (ar, ag, ab))
    venti_edited = BytesIO()
    origin.save(venti_edited, format="png")
    venti_edited.seek(0)
    return send_file(venti_edited, mimetype="image/png", as_attachment=False, attachment_filename="venti_edited.png")


if __name__ == "__main__":
    app.run(port=14514, debug=True)
