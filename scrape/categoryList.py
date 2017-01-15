class categoryList:
    def __init__(self):
        self.list = [["computers"],
            ["computers", "laptops-ultrabooks"],
            ["computers", "desktops"],
            ["computers", "accessories-add-ons"],
            ["computers", "monitors"],
            ["computers", "networking-servers"],
            ["computers", "software"],
            ["computers", "printers"],
            ["electronics"],
            ["electronics", "hdtvs-home-theater"],
            ["electronics", "cameras-camcorders"],
            ["electronics", "speakers-headphones"],
            ["tablets-phones"],
            ["tablets-phones", "accessories-apps"],
            ["tablets-phones", "tablets"],
            ["tablets-phones", "unlocked-phones"],
            ["gaming"],
            ["gaming", "games"],
            ["gaming", "hardware"],
            ["lifestyle-home"],
            ["lifestyle-home", "accessories-watches"],
            ["lifestyle-home", "automotive"],
            ["lifestyle-home", "clothing-shoes"],
            ["lifestyle-home", "entertainment"],
            ["lifestyle-home", "gadgets-novelty"],
            ["lifestyle-home", "health-fitness"],
            ["lifestyle-home", "home-outdoors"],
            ["lifestyle-home", "home-improvement-tools-garden"],
            ["movie-music-book"],
            ["amazon-best"]]

    @property
    def categoryList(self):
        return self.list