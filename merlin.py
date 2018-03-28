from body.body import Body
from body.mouth import Mouth
from body.ears import Ears
from body.head import Head

if __name__ == "__main__":
    Merlin = Body()
    # Merlin.head.mouth.say('Cześć Adam!')
    while True:
        Merlin.head.think(voice=False)
