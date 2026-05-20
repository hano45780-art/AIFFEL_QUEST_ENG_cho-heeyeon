def is_palindrome(word):
    s = str(word)
    return s == s[::-1]


def palindrome_classifier(words):
    result = {"회문": [], "회문X": []}

    for w in words:
        if is_palindrome(w):
            result["회문"].append(w)
        else:
            result["회문X"].append(w)

    palindrome_count = len(result["회문"])
    total = len(words)
    palindrome_ratio = palindrome_count / total if total else 0.0

    return result, palindrome_count, palindrome_ratio


scores = {
    "유원영": {"국어": 94, "영어": 91, "수학": 89},
    "설진민": {"국어": 88, "영어": 96, "수학": 90},
    "신윤아": {"국어": 86, "영어": 88, "수학": 77},
    "장윤아": {"국어": 98, "영어": 76, "수학": 92},
}


def _class_subject_averages(score_dict):
    if not score_dict:
        return {}

    subjects = list(next(iter(score_dict.values())).keys())
    avg = {}
    for sub in subjects:
        vals = [v[sub] for v in score_dict.values()]
        avg[sub] = sum(vals) / len(vals)
    return avg


def _student_subject_averages(student_scores):
    if not student_scores:
        return 0.0
    vals = list(student_scores.values())
    return sum(vals) / len(vals)


def score_analysis(name):
    if name not in scores:
        raise KeyError(f"'{name}' 학생 데이터가 없습니다.")

    student = scores[name]
    class_avg_by_subject = _class_subject_averages(scores)

    lines = []
    lines.append(f"[{name} 성적 분석]")

    for subject in ["국어", "영어", "수학"]:
        score = float(student[subject])
        class_avg = float(class_avg_by_subject[subject])
        diff = score - class_avg
        lines.append(
            f"{subject}: {int(score)}점, 학급 평균({class_avg:.2f}점) 대비 {diff:+.2f}"
        )

    lines.append("")

    student_avg = _student_subject_averages(student)
    class_overall_avg = sum(_student_subject_averages(s) for s in scores.values()) / len(scores)
    overall_diff = student_avg - class_overall_avg

    lines.append(
        f"전과목 평균: {student_avg:.2f}점, 학급 평균({class_overall_avg:.2f}점) 대비 {overall_diff:+.2f}"
    )

    return "\n".join(lines)


if __name__ == "__main__":
    # Q1-1
    target1 = "아만남다다남만아"
    target2 = "아름다운날들부터"
    print(is_palindrome(target1))
    print(is_palindrome(target2))

    # Q1-2
    targets = [
        "기러기",
        "개미",
        "토마토",
        "스윗쏘스",
        "스위스",
        "인도인",
        "한국인",
        "벌벌벌",
        "우영우",
        "우분우",
    ]
    print(palindrome_classifier(targets))

    # Q2-2
    print(score_analysis("설진민"))
