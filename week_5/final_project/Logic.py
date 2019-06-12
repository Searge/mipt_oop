import Service


class GameEngine:
    objects = []
    map = None
    hero = None
    level = -1
    working = True
    subscribers = set()
    score = 0.
    game_process = True
    show_help = False

    def subscribe(self, obj):
        self.subscribers.add(obj)

    def unsubscribe(self, obj):
        if obj in self.subscribers:
            self.subscribers.remove(obj)

    def notify(self, message):
        for i in self.subscribers:
            i.update(message)

    # HERO
    def add_hero(self, hero):
        self.hero = hero

    def interact(self):
        for obj in self.objects:
            if list(obj.position) == self.hero.position:
                self.delete_object(obj)
                obj.interact(self, self.hero)

    # MOVEMENT
    def move_up(self):
        self.score -= 0.02
        _up = self.map[self.hero.position[1] - 1][self.hero.position[0]]
        if _up == Service.wall:
            return
        self.hero.position[1] -= 1
        self.interact()

    def move_down(self):
        self.score -= 0.02
        _down = self.map[self.hero.position[1] + 1][self.hero.position[0]]
        if _down == Service.wall:
            return
        self.hero.position[1] += 1
        self.interact()

    def move_left(self):
        self.score -= 0.02
        _left = self.map[self.hero.position[1]][self.hero.position[0] - 1]
        if _left == Service.wall:
            return
        self.hero.position[0] -= 1
        self.interact()

    def move_right(self):
        self.score -= 0.02
        _right = self.map[self.hero.position[1]][self.hero.position[0] + 1]
        if _right == Service.wall:
            return
        self.hero.position[0] += 1
        self.interact()

    # MAP
    def load_map(self, game_map):
        self.map = game_map

    # OBJECTS
    def add_object(self, obj):
        self.objects.append(obj)

    def add_objects(self, objects):
        self.objects.extend(objects)

    def delete_object(self, obj):
        self.objects.remove(obj)
