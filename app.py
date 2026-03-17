from analyzer import analyze_resume, compare_resume_with_job
from utils import read_text_file, file_exists, save_json_file


def get_valid_file_path(message: str) -> str:
    while True:
        file_path = input(message).strip()

        if file_exists(file_path):
            return file_path

        print("File not found. Please enter a valid file path.\n")


def print_resume_analysis(result: dict) -> None:
    print("\n===== RESUME ANALYSIS =====\n")

    print("Professional Summary:")
    print(result["professional_summary"])
    print()

    print("Key Technical Skills:")
    if result["key_technical_skills"]:
        print(", ".join(result["key_technical_skills"]))
    else:
        print("No clear technical skills detected")
    print()

    print("Strengths:")
    for item in result["strengths"]:
        print(f"- {item}")
    print()

    print("Weaknesses:")
    for item in result["weaknesses"]:
        print(f"- {item}")
    print()

    print("Suggestions for Improvement:")
    for item in result["suggestions_for_improvement"]:
        print(f"- {item}")


def print_job_matching(result: dict) -> None:
    print("\n===== JOB MATCHING =====\n")

    print("Match Score:")
    print(f'{result["match_score"]}/100')
    print()

    print("Matching Skills:")
    if result["matching_skills"]:
        print(", ".join(result["matching_skills"]))
    else:
        print("No strong matching skills found")
    print()

    print("Missing Skills:")
    if result["missing_skills"]:
        print(", ".join(result["missing_skills"]))
    else:
        print("No major missing skills detected")
    print()

    print("Final Evaluation:")
    print(result["final_evaluation"])


def main():
    print("AI Resume Analyzer")
    print("------------------\n")

    resume_path = get_valid_file_path("Enter resume file path: ")
    job_description_path = get_valid_file_path("Enter job description file path: ")

    resume_text = read_text_file(resume_path)
    job_description_text = read_text_file(job_description_path)

    analysis_result = analyze_resume(resume_text)
    matching_result = compare_resume_with_job(resume_text, job_description_text)

    print_resume_analysis(analysis_result)
    print_job_matching(matching_result)

    final_output = {
        "resume_analysis": analysis_result,
        "job_matching": matching_result,
    }

    save_json_file(final_output, "output.json")
    print("\nResults saved to output.json")


if __name__ == "__main__":
    main()