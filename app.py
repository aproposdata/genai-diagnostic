

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        answers = {
            "structured_data": request.form.get("structured_data"),
            "use_case": request.form.get("use_case"),
            "team_familiar": request.form.get("team_familiar"),
            "exec_sponsor": request.form.get("exec_sponsor"),
            "infra_ready": request.form.get("infra_ready")
        }

        score = sum(1 for val in answers.values() if val == "Yes")

        if score <= 2:
            result = "🔒 Not Ready"
            recommendation = "Focus on foundational data, team education, and internal alignment."
        elif score <= 4:
            result = "🧠 Somewhat Ready"
            recommendation = "Pilot well-scoped GenAI experiments tied to clear goals."
        else:
            result = "🚀 Ready"
            recommendation = "You’re in a strong position to invest in GenAI initiatives."

        return render_template("index.html", result=result, recommendation=recommendation, answers=answers)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)

