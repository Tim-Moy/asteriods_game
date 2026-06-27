import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
    
    def split(self) -> None:
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        
        spawn_angle = random.uniform(20.0, 50.0)
        
        asteroid1_vector = self.velocity.rotate(spawn_angle)
        asteroid2_vector = self.velocity.rotate(-spawn_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid1.velocity = asteroid1_vector * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid2.velocity = asteroid2_vector * 1.2