from colorama import init, Fore, Back, Style
import random

# Инициализация colorama
init()

class AsciiLetters:
    LETTERS = {
        'А': [
            ' ### ',
            '#   #',
            '#####',
            '#   #',
            '#   #'
        ],
        'Б': [
            '#### ',
            '#    ',
            '#### ',
            '#   #',
            '#### '
        ],
        'В': [
            '#### ',
            '#   #',
            '#### ',
            '#   #',
            '#### '
        ],
        'Г': [
            '#####',
            '#    ',
            '#    ',
            '#    ',
            '#    '
        ],
        'Д': [
            '  ### ',
            ' #   #',
            '#    #',
            '######',
            '#    #'
        ],
        'Е': [
            '#####',
            '#    ',
            '#### ',
            '#    ',
            '#####'
        ],
        'Ё': [
            '# # #',
            '#####',
            '#    ',
            '#### ',
            '#####'
        ],
        'Ж': [
            '#   #',
            ' # # ',
            '  #  ',
            ' # # ',
            '#   #'
        ],
        'З': [
            '#### ',
            '    #',
            ' ### ',
            '    #',
            '#### '
        ],
        'И': [
            '#   #',
            '#  ##',
            '# # #',
            '##  #',
            '#   #'
        ],
        'Й': [
            ' ### ',
            '#   #',
            '#  ##',
            '# # #',
            '#   #'
        ],
        'К': [
            '#   #',
            '#  # ',
            '###  ',
            '#  # ',
            '#   #'
        ],
        'Л': [
            ' ####',
            '#   #',
            '#   #',
            '#   #',
            '#   #'
        ],
        'М': [
            '#   #',
            '## ##',
            '# # #',
            '#   #',
            '#   #'
        ],
        'Н': [
            '#   #',
            '#   #',
            '#####',
            '#   #',
            '#   #'
        ],
        'О': [
            ' ### ',
            '#   #',
            '#   #',
            '#   #',
            ' ### '
        ],
        'П': [
            '#####',
            '#   #',
            '#   #',
            '#   #',
            '#   #'
        ],
        'Р': [
            '#### ',
            '#   #',
            '#### ',
            '#    ',
            '#    '
        ],
        'С': [
            ' ####',
            '#    ',
            '#    ',
            '#    ',
            ' ####'
        ],
        'Т': [
            '#####',
            '  #  ',
            '  #  ',
            '  #  ',
            '  #  '
        ],
        'У': [
            '#   #',
            '#   #',
            ' ### ',
            '    #',
            '#### '
        ],
        'Ф': [
            ' ### ',
            '# # #',
            '# # #',
            '# # #',
            ' ### '
        ],
        'Х': [
            '#   #',
            ' # # ',
            '  #  ',
            ' # # ',
            '#   #'
        ],
        'Ц': [
            '#   #',
            '#   #',
            '#   #',
            '#####',
            '    #'
        ],
        'Ч': [
            '#   #',
            '#   #',
            ' ####',
            '    #',
            '    #'
        ],
        'Ш': [
            '#   #',
            '#   #',
            '# # #',
            '#####',
            '#   #'
        ],
        'Щ': [
            '#   #',
            '#   #',
            '# # #',
            '#####',
            '    #'
        ],
        'Ь': [
            '#    ',
            '#    ',
            '#### ',
            '#   #',
            '#### '
        ],
        'Ы': [
            '#   #',
            '#   #',
            '#### ',
            '#   #',
            '#### '
        ],
        'Э': [
            '#### ',
            '    #',
            ' ####',
            '    #',
            '#### '
        ],
        'Ю': [
            '# ###',
            '##   #',
            '##   #',
            '##   #',
            '# ###'
        ],
        'Я': [
            '#### ',
            '#   #',
            '#### ',
            '#  # ',
            '#   #'
        ],
        ' ': [
            '     ',
            '     ',
            '     ',
            '     ',
            '     '
        ]
    }

    # Добавляем цвета
    COLORS = [
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE
    ]

    BACKGROUNDS = [
        Back.BLACK,
        Back.BLUE,
        Back.RED,
        Back.GREEN,
        Back.MAGENTA
    ]

class Canvas:
    def __init__(self, width, height, background_color=Back.BLACK):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.canvas = [[' ' for _ in range(width)] for _ in range(height)]
        self.colors = [[Fore.WHITE for _ in range(width)] for _ in range(height)]

    def draw_letter(self, letter, start_x, start_y, color=Fore.WHITE):
        if letter.upper() not in AsciiLetters.LETTERS:
            return
        
        letter_pattern = AsciiLetters.LETTERS[letter.upper()]
        for y, row in enumerate(letter_pattern):
            for x, char in enumerate(row):
                if x + start_x < self.width and y + start_y < self.height:
                    self.canvas[y + start_y][x + start_x] = char
                    self.colors[y + start_y][x + start_x] = color

    def draw_point(self, x, y, char='#'):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.canvas[y][x] = char

    def draw_line(self, x1, y1, x2, y2, char='*'):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1

        if dx > dy:
            err = dx / 2
            while x != x2:
                self.draw_point(x, y, char)
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2
            while y != y2:
                self.draw_point(x, y, char)
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        self.draw_point(x, y, char)

    def draw_rectangle(self, x1, y1, x2, y2, char='*'):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.draw_point(x, y1, char)
            self.draw_point(x, y2, char)
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.draw_point(x1, y, char)
            self.draw_point(x2, y, char)

    def display(self):
        print(self.background_color, end='')
        for row_chars, row_colors in zip(self.canvas, self.colors):
            for char, color in zip(row_chars, row_colors):
                print(f"{color}{char}", end='')
            print(Style.RESET_ALL)
        print(Style.RESET_ALL, end='')

def text_to_ascii_art(text):
    max_letter_width = max(len(pattern[0]) for pattern in AsciiLetters.LETTERS.values())
    letter_spacing = 1
    
    canvas_width = (max_letter_width + letter_spacing) * len(text)
    canvas_height = 5

    # Случайный цвет фона
    background = random.choice(AsciiLetters.BACKGROUNDS)
    canvas = Canvas(canvas_width, canvas_height, background)
    
    for i, char in enumerate(text):
        # Случайный цвет для каждой буквы
        color = random.choice(AsciiLetters.COLORS)
        canvas.draw_letter(char, i * (max_letter_width + letter_spacing), 0, color)
    
    return canvas

def main():
    text = input('Введите текст (русскими буквами): ')
    canvas = text_to_ascii_art(text)
    canvas.display()

if __name__ == '__main__':
    main() 