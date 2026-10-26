import logging
import os

from flask import Flask, jsonify

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "service": "cndp-advanced",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "message": "Cloud-Native Delivery Platform is running",
    }), 200


@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.get("/ready")
def ready():
    return jsonify({"status": "ready"}), 200


@app.get("/info")
def info():
    logger.info("Application info endpoint requested")
    return jsonify({
        "service": "cndp-advanced",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("APP_ENV", "development"),
    }), 200


@app.errorhandler(404)
def not_found(_error):
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
