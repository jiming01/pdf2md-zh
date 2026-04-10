import os
from pathlib import Path
from pdf2md.pdf2md import PDF2MD

def main():
    input_path = "./pdf/paper.pdf"
    basename = Path(input_path).stem
    output_path = os.path.join("./md", basename)
    os.makedirs(output_path, exist_ok=True)

    agent = PDF2MD(input_path, output_path)
    agent.pdf2md()

if __name__ == "__main__":
    main()





