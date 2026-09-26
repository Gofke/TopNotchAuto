# Real vehicle inventory — model names and Facebook post links confirmed by the client.
# Each vehicle links out to its Facebook post, where the client keeps full details
# (specs, price, availability) up to date.
# No specs are asserted here — all details live on Facebook.
# crop: per-photo object-position hint for the 4:3 card crop (None = default center)

VEHICLES = [
    {
        "id": "ford-ecosport",
        "img": "ford_ecosport_blue.jpg",
        "crop": "mid-low",
        "name": "Ford EcoSport",
        "fb": "https://www.facebook.com/story.php?story_fbid=1707829041348224&id=100063634327375",
    },
    {
        "id": "jeep-renegade",
        "img": "jeep_renegade_black.jpg",
        "crop": "mid-low",
        "name": "Jeep Renegade",
        "fb": "https://www.facebook.com/story.php?story_fbid=1707844644679997&id=100063634327375",
    },
    {
        "id": "toyota-sienta-green",
        "img": "toyota_mpv_green.jpg",
        "crop": None,
        "name": "Toyota Sienta",
        "fb": "https://www.facebook.com/story.php?story_fbid=1707897311341397&id=100063634327375",
    },
    {
        "id": "toyota-sienta-brown",
        "img": "toyota_mpv_brown.jpg",
        "crop": None,
        "name": "Toyota Sienta",
        "fb": "https://www.facebook.com/story.php?story_fbid=1707894534675008&id=100063634327375",
    },
    {
        "id": "toyota-passo-moda",
        "img": "toyota_passo_red_rear.jpg",
        "crop": None,
        "name": "Toyota Passo Moda",
        "fb": "https://www.facebook.com/story.php?story_fbid=1707849724679489&id=100063634327375",
    },
    {
        "id": "toyota-corolla-axio",
        "img": "toyota_sedan_white.jpg",
        "crop": None,
        "name": "Toyota Corolla Axio",
        "fb": "https://www.facebook.com/story.php?story_fbid=1707840514680410&id=100063634327375",
    },
    {
        "id": "mazda-axela-sedan",
        "img": "mazda3_silver.jpg",
        "crop": "low",
        "name": "Mazda Axela Sedan",
        "fb": "https://www.facebook.com/story.php?story_fbid=1707837544680707&id=100063634327375",
    },
    {
        "id": "nissan-clipper-van",
        "img": "nissan_van_silver.jpg",
        "crop": "high",
        "name": "Nissan Clipper Mini Utility Van",
        "fb": "https://www.facebook.com/story.php?story_fbid=1707833274681134&id=100063634327375",
    },
]

FEATURED_VEHICLE = VEHICLES[0]  # Ford EcoSport
