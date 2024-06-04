import sys

from paracrine.runner import run
import desktop
import zoom
import sound
import deborphan

if __name__ == "__main__":
    run(
        sys.argv[1:],
        [
            desktop,
            zoom,
            sound,
            deborphan
        ],
    )
