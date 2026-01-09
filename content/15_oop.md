# 15. The Blueprint: Classes & OOP

> "I am inevitable." - Thanos
> "I am Iron Man." - Tony Stark

Object-Oriented Programming (OOP) allows you to create your own types of data. You build a "Blueprint" (Class) and create "Instances" (Objects) from it.

## 1. The Class (The Blueprint)
Tony Stark has a blueprint for the Iron Man suit.

```python
class IronManSuit:
    # The Constructor (runs when you build the suit)
    def __init__(self, model_name, flight_ready):
        self.model = model_name
        self.flight_ready = flight_ready
        self.battery = 100
    
    # A Method (Action)
    def fly(self):
        if self.flight_ready and self.battery > 0:
            print(f"{self.model} is taking off!")
            self.battery -= 10
        else:
            print("Systems failing.")

    def status(self):
        print(f"Model: {self.model} | Battery: {self.battery}%")
```

## 2. The Object (The Suit)
The blueprint isn't the suit. You have to build it.

```python
mark85 = IronManSuit("Mark 85", True)
mark1 = IronManSuit("Mark 1", False)

mark85.fly() # Mark 85 is taking off!
mark1.fly()  # Systems failing.
```

## 3. Inheritance (Legacy)
Spider-Man's suit inherits tech from Iron Man's suit but adds its own features.

```python
class SpiderSuit(IronManSuit):
    def __init__(self, model_name, instant_kill_mode):
        # Initialize the parent (Iron Man tech)
        super().__init__(model_name, True) 
        self.instant_kill = instant_kill_mode
    
    def shoot_web(self):
        print("Thwip!")
```

```python
iron_spider = SpiderSuit("Iron Spider", True)
iron_spider.fly()      # Inherited from IronManSuit
iron_spider.shoot_web() # Exclusive to SpiderSuit
```

---
**Next Step:** Manipulating reality (Decorators).
