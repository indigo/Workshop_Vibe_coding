import os

def concatenate_blocks():
    output_path = "docs/presentation/all_blocks.md"
    output_content = ""

    # Section 1: Hook / Introduction
    output_content += r"# SECTION 1: Hook / Introduction - Your Vision & The AI Context" + os.linesep + os.linesep
    for i in range(1, 6):
        block_path = f"docs/presentation/block{i}/block{i}.md"
        try:
            with open(block_path, "r") as f:
                block_content = f.read()
                output_content += block_content + os.linesep + os.linesep
        except FileNotFoundError:
            print(f"File not found: {block_path}")
            continue
    output_content += "---" + os.linesep + os.linesep

    # Section 2: The Why - Challenges & Opportunities
    output_content += r"# SECTION 2: \"THE WHY\" - Challenges & Opportunities (The Chess Analogy)" + os.linesep + os.linesep
    for i in range(6, 10):
        block_path = f"docs/presentation/block{i}/block{i}.md"
        try:
            with open(block_path, "r") as f:
                block_content = f.read()
                output_content += block_content + os.linesep + os.linesep
        except FileNotFoundError:
            print(f"File not found: {block_path}")
            continue
    output_content += "---" + os.linesep + os.linesep

    # Section 3: The What - Your Solution
    output_content += r"# SECTION 3: \"THE WHAT\" - Your Solution (The Need for Description & Approval)" + os.linesep + os.linesep
    for i in range(10, 16):
        block_path = f"docs/presentation/block{i}/block{i}.md"
        try:
            with open(block_path, "r") as f:
                block_content = f.read()
                output_content += block_content + os.linesep + os.linesep
        except FileNotFoundError:
            print(f"File not found: {block_path}")
            continue
    output_content += "---" + os.linesep + os.linesep

    # Section 4: The How
    output_content += r"# SECTION 4: \"THE HOW\" - Part 1: Character Example & LLM-Assisted Approval" + os.linesep + os.linesep
    for i in range(16, 22):
        block_path = f"docs/presentation/block{i}/block{i}.md"
        try:
            with open(block_path, "r") as f:
                block_content = f.read()
                output_content += block_content + os.linesep + os.linesep
        except FileNotFoundError:
            print(f"File not found: {block_path}")
            continue
    output_content += "---" + os.linesep + os.linesep

    # Section 4 (Continued): The How - Part 2
    output_content += r"# SECTION 4 (Continued): \"THE HOW\" - Part 2: Application to Game Production & Distribution" + os.linesep + os.linesep
    for i in range(22, 30):
        block_path = f"docs/presentation/block{i}/block{i}.md"
        try:
            with open(block_path, "r") as f:
                block_content = f.read()
                output_content += block_content + os.linesep + os.linesep
        except FileNotFoundError:
            print(f"File not found: {block_path}")
            continue
    output_content += "---" + os.linesep + os.linesep

    with open(output_path, "w") as outfile:
        outfile.write(output_content)
    print(f"Concatenated and sectioned all blocks into {output_path}")

if __name__ == "__main__":
    concatenate_blocks()