import json
import os
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def play():
    with open('story.json', 'r', encoding='utf-8') as f:
        story = json.load(f)

    current_scene = 'start'
    energy = 50  # Стартовый уровень энергии / кофе

    while True:
        clear_screen()
        scene = story.get(current_scene)

        if not scene:
            print('Ошибка: сцена не найдена! Пора делать коммит и дописать её.')
            break

        print(f'=== Энергия: {energy}% ===\n')
        print(scene['text'])
        print('\n' + '-' * 40)

        # Если у сцены нет вариантов выбора — это финал
        if not scene.get('choices'):
            print('\n[ КОНЕЦ ИГРЫ ]')
            break

        for i, choice in enumerate(scene['choices'], 1):
            print(f"{i}. {choice['text']}")

        try:
            answer = int(input('\nТвой выбор (введи номер): ')) - 1
            if 0 <= answer < len(scene['choices']):
                chosen = scene['choices'][answer]
                energy += chosen.get('energy_change', 0)
                current_scene = chosen['next_scene']

                if energy <= 0:
                    clear_screen()
                    print(
                        '=== Энергия: 0% ===\n\nТы уснул прямо лицом на'
                        ' клавиатуре. Сон победил.'
                    )
                    print('\n[ КОНЕЦ ИГРЫ ]')
                    break
            else:
                print('Нет такого варианта!')
                time.sleep(1)
        except ValueError:
            print('Введи нормальную цифру, ты же программист!')
            time.sleep(1)


if __name__ == '__main__':
    play()