# personalization-bias-detector
Tool to analyze potential quality differences in AI responses across dialects and demographic cues.

# AI Response Annotation Tool (Arabic)

**Author:** BOUZEROUATA Issam Salah Eddine  
**Language:** Python 3  
**Topic:** AI Data Annotation & Evaluation

---

## What This Project Does

This is a command-line annotation tool designed to help human evaluators review and rate AI-generated Arabic text responses. It was built to simulate the kind of quality evaluation workflow used in RLHF (Reinforcement Learning from Human Feedback) pipelines — where human annotators provide structured ratings that teach AI models to produce better outputs.

The tool walks an annotator through a set of AI responses and asks them to rate each one on four criteria:

| Criterion | What it measures |
|---|---|
| **Helpfulness** | Did the AI actually answer what was asked? |
| **Fluency** | Does the Arabic sound natural to a native speaker? |
| **Cultural fit** | Is the response appropriate for an Arabic-speaking audience? |
| **Accuracy** | Is the information factually correct? |

All results are saved to a CSV file and a summary of average scores can be viewed at any time.

---

## Why I Built This

Most open-source annotation tools I found were designed for English. Arabic has unique evaluation challenges — a response can be grammatically correct but feel unnatural to a native speaker, or be technically accurate but miss important cultural context (for example, giving advice that doesn't fit the local norms of an Arabic-speaking user). This tool is a starting point for thinking about annotation workflows that take those challenges seriously.

The sample responses included in the script are intentionally varied — one of them is a response that answers in English to an Arabic prompt, which is a real failure mode in Arabic-language AI systems.

---

## How to Use It

### Requirements
- Python 3.6+
- No external libraries needed

### Run the script
```bash
python ai_annotation_tool.py
```

You will see a simple menu. Choose option **1** to annotate the included sample responses. Ratings are entered interactively (1–5 scale). When done, choose option **2** to see a summary of average scores.

---

## Output

Results are saved to `annotation_results.csv` in the same folder. Each row contains the response ID, prompt, AI response, all four ratings, an optional comment, and a timestamp.

---

## Example Summary Output

```
Annotation Summary — 3 responses annotated
-----------------------------------------------------------------
  Average helpfulness          : 3.67 / 5
  Average fluency              : 3.33 / 5
  Average cultural_fit         : 3.00 / 5
  Average accuracy             : 4.00 / 5
```

---

## Future Plans

- Add support for loading response batches from a JSON file
- Add inter-annotator agreement scoring (Cohen's Kappa)
- Build a simple web interface using Flask

---

## Project Status
Beginner project — built and tested locally. Contributions and suggestions welcome.

