import json


def load_candidates() -> list[dict]:
    """загрузка данных из файла"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


def format_candidates(candidates: list[dict]) -> str:
    """список кандидатов"""
    result = '<pre>'

    for candidate in candidates:
        result += f"""
            {candidate['name']}\n
            {candidate['position']}\n
            {candidate['skills']}\n
        """
    result += '</pre>'
    return result


def get_all() -> list[dict]:
    """покажет всех кандидатов"""
    return load_candidates()


def get_by_pk(pk: int) -> dict | None:
    """вернет кандидата по pk"""
    candidates = get_all()
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate
    return None


def get_by_skill(skill: str) -> list[dict]:
    """вернет кандидатов по навыку"""
    candidates = get_all()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)

    return result
