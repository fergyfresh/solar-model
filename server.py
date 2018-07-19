from solar_model import app
import os


if __name__== "__main__":
    port = int(os.environ.get("PORT", 4000))
    app.run(host="127.0.0.1", port=port, debug=True)
