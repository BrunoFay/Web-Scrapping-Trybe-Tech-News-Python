# Requisito 12
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_title, search_by_date
from tech_news.analyzer.search_engine import search_by_tag, search_by_category
from tech_news.analyzer.ratings import top_5_categories, top_5_news
import sys


def check_if_option_is_valid(option):
    range_options = range(0, 8)
    if(not option.isnumeric() or int(option) not in range_options):
        print("Opção inválida", file=sys.stderr)
        return 'error'
    else:
        return


def option_even(option):
    if option == '0':
        number = int(input("Digite quantas notícias serão buscadas:"))
        return get_tech_news(number)
    elif option == '2':
        date = input("Digite a data no formato aaaa-mm-dd:")
        return search_by_date(date)
    elif option == '4':
        category = input("Digite a categoria:")
        return search_by_category(category)
    elif option == '6':
        return top_5_categories()


def option_odd(option):
    if option == '1':
        title = input("Digite o título:")
        return search_by_title(title)

    elif option == '3':
        tag = input("Digite a tag:")
        return search_by_tag(tag)

    elif option == '5':
        return top_5_news()


def analyzer_menu():
    """Seu código deve vir aqui"""
    input_messages = [
        'Selecione uma das opções a seguir:\n',
        '0 - Popular o banco com notícias;\n',
        '1 - Buscar notícias por título;\n',
        '2 - Buscar notícias por data;\n',
        '3 - Buscar notícias por tag;\n',
        '4 - Buscar notícias por categoria;\n',
        '5 - Listar top 5 notícias;\n',
        '6 - Listar top 5 categorias;\n',
        '7 - Sair.'
    ]
    while True:
        selection = input(" ".join(input_messages))

        check_option = check_if_option_is_valid(selection)
        if check_option:
            return check_option
        if selection == '7':
            print('Encerrando script')
            break
        if(int(selection) % 2 == 0):
            return option_even(selection)
        else:
            return option_odd(selection)
