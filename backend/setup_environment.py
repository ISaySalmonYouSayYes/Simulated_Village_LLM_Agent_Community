import subprocess


def install_packages():
    """Install required Python packages."""
    required_packages = [
        "langchain",
        "langchain_openai",
        "langchain_experimental",
        "langchainhub",
        "sentence-transformers",
        "langgraph",
        "flask",
        "flask-cors",
        "langsmith"
    ]

    for package in required_packages:
        try:
            print(f"Installing {package}...")
            subprocess.run(["pip", "install", package], check=True)
            print(f"Successfully installed {package}.")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}. Please install it manually.")


if __name__ == "__main__":
    install_packages()
