import pytest
import pygame
from Pelea import Fighter

@pytest.fixture(scope="module")
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()

def test_fighter_initialization():
    fighter = Fighter(100, 200)
    assert fighter.rect.x == 100
    assert fighter.rect.y == 200

def test_move_p1_right():
    fighter = Fighter(100, 200)
    key_mock = {pygame.K_d: True}
    pygame.key.get_pressed = lambda: key_mock
    fighter.move_p1(800, 600, pygame.Surface((800, 600)))
    assert fighter.rect.x > 100

def test_move_p1_left():
    fighter = Fighter(100, 200)
    key_mock = {pygame.K_a: True}
    pygame.key.get_pressed = lambda: key_mock
    fighter.move_p1(800, 600, pygame.Surface((800, 600)))
    assert fighter.rect.x < 100

def test_move_p1_jump():
    fighter = Fighter(100, 200)
    key_mock = {pygame.K_w: True}
    pygame.key.get_pressed = lambda: key_mock
    fighter.move_p1(800, 600, pygame.Surface((800, 600)))
    assert fighter.jump is True

def test_move_p2_right():
    fighter = Fighter(300, 400)
    key_mock = {pygame.K_RIGHT: True}
    pygame.key.get_pressed = lambda: key_mock
    fighter.move_p2(800, 600)
    assert fighter.rect.x > 300

def test_move_p2_left():
    fighter = Fighter(300, 400)
    key_mock = {pygame.K_LEFT: True}
    pygame.key.get_pressed = lambda: key_mock
    fighter.move_p2(800, 600)
    assert fighter.rect.x < 300

def test_move_p2_jump():
    fighter = Fighter(300, 400)
    key_mock = {pygame.K_UP: True}
    pygame.key.get_pressed = lambda: key_mock
    fighter.move_p2(800, 600)
    assert fighter.jump is True

def test_attack():
    surface = pygame.Surface((800, 600))
    fighter = Fighter(400, 300)
    fighter.attack(surface)
    attack_rect = pygame.Rect(fighter.rect.centerx, fighter.rect.y, 2 * fighter.rect.width, fighter.rect.height)
    color_at_center = surface.get_at(attack_rect.center)
    assert color_at_center == (0, 0, 255)

def test_draw_p1():
    surface = pygame.Surface((800, 600))
    fighter = Fighter(400, 300)
    fighter.draw_p1(surface)
    pixel_color = surface.get_at((fighter.rect.x, fighter.rect.y))
    assert pixel_color == (255, 0, 0)

def test_draw_p2():
    surface = pygame.Surface((800, 600))
    fighter = Fighter(400, 300)
    fighter.draw_p2(surface)
    pixel_color = surface.get_at((fighter.rect.x, fighter.rect.y))
    assert pixel_color == (0, 255, 0)
