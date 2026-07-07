def generate_report(target, findings):
    with open("reports/report.txt", "w") as report:
        report.write("SQL Injection Scanner Report\n")
        report.write("=" * 40 + "\n")
        report.write(f"Target: {target}\n\n")

        if findings:
            for finding in findings:
                report.write(f"- {finding}\n")
        else:
            report.write("No findings recorded.\n")
