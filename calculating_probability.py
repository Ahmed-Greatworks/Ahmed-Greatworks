import random
import copy

class Hat:
    def __init__(self, **balls):
        """Initialize the hat with balls."""
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        """Draw a specified number of balls from the hat and remove them from contents."""
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents.clear()
            return drawn_balls
        
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Run the experiment a specified number of times and return the probability of drawing the expected balls."""
    success_count = 0
    
    for _ in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        drawn_balls = temp_hat.draw(num_balls_drawn)
        drawn_counts = {color: drawn_balls.count(color) for color in set(drawn_balls)}
        
        if all(drawn_counts.get(color, 0) >= count for color, count in expected_balls.items()):
            success_count += 1
    
    return success_count / num_experiments

# Example usage
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={'red': 2, 'green': 1}, num_balls_drawn=5, num_experiments=2000)
print(probability)
