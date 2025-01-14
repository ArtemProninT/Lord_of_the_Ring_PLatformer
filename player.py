from baze import *


class Player(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__()
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

        self.level_map = []

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

    def animate(self):
        # TODO сделать здесь анимацию
        pass

    def move(self, movement):
        if movement == "up":
            if self.y > 0 and self.level_map[self.y - 1][self.x] == ".":
                self.y += 1
        elif movement == "left":
            if self.x > 0 and self.level_map[self.y][self.x - 1] == ".":
                self.x -= 1
        elif movement == "right":
            if self.x < 1 and self.level_map[self.y][self.x + 1] == ".":
                self.x += 1

        # TODO код вставить в часть обработки событий
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = False
        #     elif event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_UP:
        #             player.move("up")
        #         elif event.key == pygame.K_LEFT:
        #             player.move("left")
        #         elif event.key == pygame.K_RIGHT:
        #             player.move("right")


    def damage(self):
        # TODO сделать здесь алгоритм получения урона
        pass


    # TODO понять и сделать остальные фенкции
