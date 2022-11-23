from flask import Flask
from utils import get_all, format_candidates, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route("/")
def page_index():
    """Главная страница"""
    candidates: list[dict] = get_all()
    result: str = format_candidates(candidates)
    return result


@app.route("/candidate/<int:pk>")
def page_candidate(pk):
    """Поиск по pk"""
    candidate: dict = get_by_pk(pk)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result


@app.route("/skills/<skill>")
def page_skills(skill):
    """Поиск по навыку"""
    skill_lower = skill.lower()
    candidates: list[dict] = get_by_skill(skill_lower)
    result = format_candidates(candidates)
    return result


app.run()
