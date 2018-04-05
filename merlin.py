from body.body import Body

if __name__ == "__main__":
    voice = True
    # voice = False
    Merlin = Body(voice=voice)
    # Merlin.head.mouth.say('Cześć Adam!')
    while True:
        Merlin.head.think()
