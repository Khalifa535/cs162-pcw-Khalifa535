from pathlib import Path

import requests


BASE_URL = "https://httpbin.org"
OUTPUT_DIR = Path(__file__).parent


def print_response(label, response):
    print(f"\n== {label} ==")
    print(f"request: {response.request.method} {response.request.url}")
    print(f"status: {response.status_code}")
    print(f"response headers: {dict(response.headers)}")


def basic_auth_demo():
    response = requests.get(
        f"{BASE_URL}/basic-auth/khalifa/session5",
        auth=("khalifa", "session5"),
        timeout=10,
    )
    print_response("Basic auth", response)
    print(response.json())


def image_download_demo():
    response = requests.get(f"{BASE_URL}/image/png", timeout=10)
    print_response("Image download", response)
    image_path = OUTPUT_DIR / "httpbin-image.png"
    image_path.write_bytes(response.content)
    print(f"saved image bytes: {len(response.content)}")
    print(f"saved to: {image_path}")


def uuid_demo():
    response = requests.get(f"{BASE_URL}/uuid", timeout=10)
    print_response("UUID4", response)
    print(response.json())


def simple_json_demo():
    response = requests.get(f"{BASE_URL}/json", timeout=10)
    print_response("Simple JSON", response)
    data = response.json()
    print(data)
    print(f"slideshow title: {data['slideshow']['title']}")


def main():
    basic_auth_demo()
    image_download_demo()
    uuid_demo()
    simple_json_demo()


if __name__ == "__main__":
    main()
