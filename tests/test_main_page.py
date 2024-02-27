import allure
import pytest

from data import DataAnswers


class TestMainPage:
    @allure.title('Проверка ответов на Вопросы о важном {item}')
    @pytest.mark.parametrize("item, expected_text", [
        (0, DataAnswers.answer_0),
        (1, DataAnswers.answer_1),
        (2, DataAnswers.answer_2),
        (3, DataAnswers.answer_3),
        (4, DataAnswers.answer_4),
        (5, DataAnswers.answer_5),
        (6, DataAnswers.answer_6),
        (7, DataAnswers.answer_7),
    ])
    def test_question_about_important_answer_success(self, main_page, item, expected_text):
        text_answer = main_page.question_get_text_after_click(item)
        assert text_answer == expected_text
