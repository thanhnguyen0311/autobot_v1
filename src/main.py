import argparse
from src.ui import create_ui  # Import the function to create the Tkinter UI
from src.bot import run_bot  # Import the bot logic for direct CLI usage


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Automation Bot Entry Point")
    parser.add_argument(
        "--cli",
        action="store_true",
        help="Run the bot in CLI mode without UI (argument required: --url)",
    )
    parser.add_argument(
        "--url",
        type=str,
        help="URL to navigate to when using CLI mode",
    )
    args = parser.parse_args()

    # Check if CLI mode is enabled
    if args.cli:
        if not args.url:
            print("Error: --url is required when using --cli mode.")
        else:
            try:
                print(f"Running the bot on URL: {args.url}")
                run_bot(args.url)  # Call the bot's logic directly with the URL
                print("Bot completed successfully!")
            except Exception as e:
                print(f"Error while running the bot: {e}")
    else:
        # Default behavior: Run the GUI
        create_ui()


if __name__ == "__main__":
    main()