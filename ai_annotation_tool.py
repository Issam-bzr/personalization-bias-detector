# ai_annotation_tool.py
# Author: BOUTEROUATA Issam Salah Eddine
# Description: A simple command-line tool to annotate and evaluate AI-generated
# Arabic text responses. Annotators can rate responses on helpfulness, fluency,
# and cultural appropriateness, and save results to a CSV file.

import csv
import json
import os
from datetime import datetime

OUTPUT_FILE = "annotation_results.csv"

# The fields we evaluate each AI response on
RATING_CRITERIA = [
    ("helpfulness", "How helpful is this response? (1=Not helpful, 5=Very helpful)"),
    ("fluency", "How natural does the Arabic sound? (1=Unnatural, 5=Perfectly natural)"),
    ("cultural_fit", "Is the response culturally appropriate for an Arabic-speaking user? (1=Not at all, 5=Fully appropriate)"),
    ("accuracy", "Is the information factually correct? (1=Many errors, 5=Fully accurate)"),
]

VALID_RATINGS = ["1", "2", "3", "4", "5"]

SAMPLE_RESPONSES = [
    {
        "id": "resp_001",
        "prompt": "ما هي عاصمة المملكة العربية السعودية؟",
        "ai_response": "عاصمة المملكة العربية السعودية هي مدينة الرياض.",
    },
    {
        "id": "resp_002",
        "prompt": "كيف أحسن مزاجي عندما أشعر بالإحباط؟",
        "ai_response": "يمكنك تحسين مزاجك عن طريق ممارسة الرياضة، والتحدث مع أصدقائك، أو الاستماع إلى الموسيقى التي تحبها.",
    },
    {
        "id": "resp_003",
        "prompt": "اقترح عليّ وصفة سهلة للإفطار.",
        "ai_response": "Try making scrambled eggs with toast. It is simple and quick to prepare in the morning.",
    },
]


def get_valid_rating(prompt_text):
    """Ask for a rating and keep asking until a valid one is given."""
    while True:
        value = input(f"  {prompt_text}: ").strip()
        if value in VALID_RATINGS:
            return int(value)
        print("  Please enter a number between 1 and 5.")


def annotate_response(response_item):
    """Walk the annotator through rating a single AI response."""
    print("\n" + "=" * 65)
    print(f"Response ID : {response_item['id']}")
    print(f"Prompt      : {response_item['prompt']}")
    print(f"AI Response : {response_item['ai_response']}")
    print("-" * 65)
    print("Please rate the following criteria:")

    ratings = {}
    for field, question in RATING_CRITERIA:
        ratings[field] = get_valid_rating(question)

    comment = input("  Any additional comment? (press Enter to skip): ").strip()

    return {
        "response_id": response_item["id"],
        "prompt": response_item["prompt"],
        "ai_response": response_item["ai_response"],
        **ratings,
        "comment": comment,
        "annotated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def save_to_csv(record):
    """Append an annotation record to the CSV output file."""
    file_exists = os.path.isfile(OUTPUT_FILE)
    with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=record.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(record)
    print(f"  ✅ Saved to {OUTPUT_FILE}")


def show_summary():
    """Read the CSV and print a simple summary of average scores."""
    if not os.path.isfile(OUTPUT_FILE):
        print("No annotation data found yet.")
        return

    records = []
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)

    if not records:
        print("No records in file.")
        return

    print("\n" + "=" * 65)
    print(f"Annotation Summary — {len(records)} responses annotated")
    print("-" * 65)

    for field, _ in RATING_CRITERIA:
        values = [int(r[field]) for r in records if r.get(field)]
        avg = sum(values) / len(values) if values else 0
        print(f"  Average {field:20}: {avg:.2f} / 5")
    print("=" * 65)


def main():
    print("\nArabic AI Response Annotation Tool")
    print("Author: BOUTEROUATA Issam Salah Eddine")
    print("=" * 65)

    while True:
        print("\nMenu:")
        print("  1 - Annotate sample responses")
        print("  2 - View summary of annotations so far")
        print("  3 - Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            for response in SAMPLE_RESPONSES:
                record = annotate_response(response)
                save_to_csv(record)
            print("\nAll sample responses annotated.")

        elif choice == "2":
            show_summary()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
