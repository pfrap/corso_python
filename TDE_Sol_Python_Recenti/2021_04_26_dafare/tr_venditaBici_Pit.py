# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'venditaBici'

# Vi forniamo un esempio di struttura dati che potrebbe
# essere restituita da una delle funzioni seguenti.
# La (vera) struttura dati caricata dal file sara' diversa:
# può essere più lunga, i primi elementi possono differire come valori.

datiBici = [
    (20, 'sella', 54), (20, 'pedale', 134), (20, 'copertone', 205),
    (20, 'bicicletta', 2047), (20, 'manopola', 161), (10, 'cambio', 113),
    (10, 'mozzo', 82), (10, 'paracatena', 60), (47, 'copertone', 158),
    (21, 'portapacchi', 135), (21, 'cavalletto', 75), (21, 'catena', 45),
    (48, 'parafango', 99), (48, 'pedale', 122), (48, 'bicicletta', 1569),
    (48, 'cambio', 110), (28, 'mozzo', 77), (28, 'copertone', 153),
    (28, 'manopola', 129), (28, 'selettore', 152), (28, 'pedale', 112),
    (28, 'freno', 141), (6, 'manopola', 130), (6, 'copertone', 200),
    (6, 'pedivella', 42), (6, 'pedale', 124), (6, 'guarnitura', 93),
    (44, 'parafango', 115), (44, 'pedivella', 58), (45, 'raggi', 57),
    (45, 'freno', 140), (45, 'sella', 46), (45, 'manopola', 116),
    (41, 'manubrio', 75), (41, 'sella', 52), (41, 'ruota', 112),
    (41, 'selettore', 156), (41, 'parafango', 90), (16, 'copertone', 181),
    (16, 'disco', 135), (16, 'cavalletto', 87), (16, 'parafango', 110),
    (16, 'pedivella', 49), (16, 'pignone', 155), (24, 'portapacchi', 144),
    (24, 'manopola', 159), (24, 'guarnitura', 103), (3, 'parafango', 88),
    (3, 'pedivella', 52), (3, 'bicicletta', 2258), (3, 'ruota', 125),
    (3, 'copertone', 181), (30, 'bicicletta', 1837), (44, 'sella', 50),
    (11, 'bicicletta', 2277), (11, 'pedivella', 49), (11, 'freno', 143),
    (11, 'raggi', 61), (11, 'sella', 54), (11, 'manubrio', 65),
    (10, 'raggi', 57), (10, 'pedale', 107), (10, 'freno', 167),
    (10, 'guarnitura', 115), (10, 'disco', 100), (10, 'portapacchi', 140),
    (35, 'bicicletta', 2162), (36, 'bicicletta', 1818), (36, 'pedale', 113),
    (36, 'pignone', 162), (36, 'paracatena', 54), (36, 'raggi', 70),
    (48, 'freno', 144), (48, 'selettore', 204), (1, 'pedale', 131),
    (1, 'freno', 178), (1, 'guarnitura', 100), (1, 'mozzo', 79),
    (1, 'pignone', 167), (1, 'paracatena', 61), (23, 'deragliatore', 203),
    (7, 'manopola', 124), (7, 'pedivella', 58), (7, 'selettore', 172),
    (7, 'raggi', 69), (7, 'paracatena', 54), (7, 'cambio', 119),
    (14, 'guarnitura', 110), (14, 'pedale', 136), (14, 'selettore', 220),
    (14, 'copertone', 184), (8, 'bicicletta', 2277), (38, 'pignone', 152),
    (45, 'pedale', 108), (45, 'copertone', 209), (45, 'manubrio', 74),
    (45, 'deragliatore', 162), (45, 'mozzo', 66), (28, 'paracatena', 71),
    (28, 'lume', 182), (28, 'bicicletta', 1799), (28, 'catena', 45),
    (28, 'manubrio', 92), (37, 'bicicletta', 2124), (37, 'pedivella', 56),
    (37, 'guarnitura', 97), (12, 'disco', 146), (12, 'portapacchi', 118),
    (12, 'pignone', 152), (12, 'bicicletta', 1971), (7, 'ruota', 140),
    (7, 'copertone', 140), (27, 'pedivella', 59), (27, 'manubrio', 85),
    (27, 'guarnitura', 128), (27, 'paracatena', 77), (27, 'copertone', 188),
    (27, 'bicicletta', 1780), (5, 'raggi', 65), (7, 'pedale', 132),
    (7, 'portapacchi', 127), (7, 'freno', 183), (7, 'disco', 147),
    (7, 'parafango', 108), (7, 'mozzo', 80), (34, 'pedale', 124),
    (34, 'pignone', 194), (45, 'parafango', 98), (45, 'lume', 147),
    (45, 'portapacchi', 169), (45, 'selettore', 191), (45, 'catena', 56),
    (45, 'pedivella', 48), (33, 'lume', 160), (27, 'cambio', 119),
    (27, 'manopola', 126), (27, 'pignone', 180), (49, 'guarnitura', 111),
    (33, 'selettore', 206), (33, 'ruota', 112), (33, 'cambio', 148),
    (33, 'pedale', 98), (23, 'cavalletto', 83), (23, 'bicicletta', 1588),
    (23, 'ruota', 101), (23, 'parafango', 109), (23, 'guarnitura', 115),
    (44, 'disco', 140), (44, 'pignone', 143), (44, 'portapacchi', 116),
    (7, 'bicicletta', 2105), (7, 'sella', 41), (7, 'lume', 199),
    (37, 'manopola', 149), (37, 'cambio', 145), (37, 'manubrio', 88),
    (43, 'lume', 189), (43, 'freno', 178), (43, 'pignone', 179),
    (43, 'pedale', 118), (8, 'lume', 140), (8, 'cavalletto', 79),
    (8, 'pedale', 112), (32, 'deragliatore', 171), (32, 'disco', 141),
    (32, 'lume', 165), (34, 'manopola', 166), (43, 'bicicletta', 1914),
    (25, 'paracatena', 59), (25, 'parafango', 85), (25, 'manubrio', 75),
    (25, 'bicicletta', 1550), (25, 'copertone', 211), (30, 'freno', 127),
    (30, 'cambio', 126), (30, 'disco', 102), (18, 'raggi', 81),
    (18, 'pignone', 153), (18, 'bicicletta', 2105), (18, 'cambio', 107),
    (18, 'cavalletto', 75), (15, 'paracatena', 59), (15, 'ruota', 126),
    (15, 'portapacchi', 172), (15, 'raggi', 62), (15, 'sella', 49),
    (15, 'pedale', 125), (1, 'catena', 52), (9, 'manubrio', 83),
    (9, 'manopola', 167), (9, 'paracatena', 69), (29, 'manopola', 129),
    (29, 'bicicletta', 2201), (29, 'ruota', 134), (11, 'parafango', 104),
    (11, 'catena', 53), (11, 'disco', 121), (11, 'deragliatore', 149),
    (11, 'selettore', 149), (11, 'pignone', 148), (19, 'bicicletta', 1665),
    (15, 'cavalletto', 85), (15, 'copertone', 161), (15, 'pedivella', 52),
    (15, 'manopola', 154), (34, 'lume', 175), (34, 'deragliatore', 214),
    (34, 'parafango', 89), (34, 'bicicletta', 2277), (34, 'cavalletto', 76),
    (43, 'ruota', 96), (43, 'mozzo', 80), (43, 'copertone', 202),
    (43, 'disco', 127), (39, 'sella', 39), (12, 'cambio', 131),
    (25, 'cavalletto', 71), (25, 'pedale', 131), (25, 'freno', 129),
    (25, 'deragliatore', 198), (25, 'selettore', 161), (25, 'pignone', 199),
    (4, 'copertone', 198), (4, 'raggi', 58), (8, 'manubrio', 79),
    (8, 'pedivella', 42), (8, 'ruota', 119), (18, 'sella', 52),
    (37, 'selettore', 160), (25, 'cambio', 128), (29, 'pedivella', 54),
    (29, 'pignone', 190), (34, 'paracatena', 71), (34, 'sella', 57),
    (34, 'ruota', 139), (34, 'disco', 123), (34, 'selettore', 215),
    (10, 'sella', 57), (10, 'selettore', 206), (10, 'bicicletta', 1990),
    (10, 'cavalletto', 85), (10, 'ruota', 97), (10, 'lume', 170),
    (25, 'raggi', 63), (34, 'manubrio', 87), (14, 'bicicletta', 1703),
    (2, 'bicicletta', 1990), (2, 'freno', 150), (2, 'disco', 98),
    (2, 'manopola', 123), (49, 'mozzo', 62), (49, 'ruota', 97),
    (49, 'pedivella', 54), (49, 'raggi', 66), (28, 'sella', 46),
    (28, 'pignone', 147), (49, 'bicicletta', 1588), (49, 'sella', 41),
    (49, 'lume', 170), (49, 'deragliatore', 180), (49, 'cambio', 128),
    (29, 'freno', 158), (9, 'bicicletta', 1875), (9, 'selettore', 184),
    (9, 'cambio', 125), (9, 'copertone', 144), (43, 'pedivella', 51),
    (43, 'parafango', 116), (43, 'sella', 47), (12, 'guarnitura', 115),
    (12, 'copertone', 181), (29, 'cambio', 108), (34, 'guarnitura', 127),
    (44, 'ruota', 115), (44, 'raggi', 75), (44, 'selettore', 176),
    (44, 'cambio', 151), (44, 'mozzo', 72), (7, 'pignone', 158),
    (7, 'guarnitura', 91), (7, 'cavalletto', 64), (7, 'manubrio', 79),
    (7, 'catena', 43), (26, 'bicicletta', 1626), (26, 'cavalletto', 84),
    (26, 'catena', 51), (17, 'bicicletta', 1646), (17, 'lume', 150),
    (17, 'paracatena', 79), (49, 'manubrio', 65), (49, 'copertone', 160),
    (47, 'bicicletta', 1933), (47, 'catena', 39), (47, 'raggi', 67),
    (47, 'mozzo', 58), (47, 'pedale', 104), (39, 'portapacchi', 125),
    (39, 'paracatena', 56), (39, 'disco', 113), (39, 'parafango', 85),
    (39, 'deragliatore', 210), (10, 'pignone', 157), (10, 'deragliatore', 167),
    (10, 'pedivella', 51), (43, 'catena', 45), (43, 'raggi', 68),
    (43, 'paracatena', 64), (20, 'ruota', 100), (33, 'raggi', 56),
    (46, 'cavalletto', 79), (46, 'bicicletta', 1952), (46, 'manubrio', 68),
    (37, 'copertone', 183), (37, 'deragliatore', 212), (37, 'sella', 40),
    (37, 'catena', 42), (25, 'disco', 135), (25, 'mozzo', 72),
    (1, 'cambio', 119), (1, 'copertone', 207), (1, 'selettore', 152),
    (1, 'cavalletto', 68), (1, 'lume', 202), (32, 'bicicletta', 2009),
    (32, 'manopola', 154), (32, 'portapacchi', 124), (32, 'freno', 160),
    (32, 'ruota', 114), (32, 'pedivella', 41), (23, 'catena', 49),
    (23, 'raggi', 70), (23, 'pignone', 184), (23, 'portapacchi', 164),
    (46, 'parafango', 97), (46, 'portapacchi', 153), (13, 'bicicletta', 2105),
    (13, 'paracatena', 58), (13, 'guarnitura', 115), (48, 'paracatena', 71),
    (31, 'mozzo', 83), (15, 'cambio', 135), (15, 'guarnitura', 111),
    (15, 'disco', 132), (47, 'freno', 183), (22, 'mozzo', 84),
    (22, 'bicicletta', 1837), (22, 'cavalletto', 81), (39, 'cambio', 151),
    (39, 'guarnitura', 120), (37, 'freno', 167), (37, 'pedale', 103),
    (18, 'copertone', 170), (18, 'selettore', 204), (4, 'bicicletta', 1760),
    (4, 'parafango', 92), (4, 'mozzo', 84), (4, 'cambio', 117),
    (8, 'pignone', 174), (8, 'paracatena', 54), (8, 'raggi', 76),
    (17, 'sella', 55), (24, 'pedivella', 45), (36, 'deragliatore', 169),
    (8, 'sella', 54), (8, 'deragliatore', 176), (8, 'mozzo', 76),
    (8, 'selettore', 152), (25, 'sella', 56), (25, 'guarnitura', 131),
    (25, 'pedivella', 55), (25, 'portapacchi', 144), (49, 'catena', 42),
    (49, 'freno', 169), (49, 'parafango', 117), (49, 'paracatena', 78),
    (49, 'manopola', 136), (16, 'bicicletta', 2124), (16, 'raggi', 65),
    (16, 'manubrio', 80), (16, 'paracatena', 73), (18, 'freno', 170),
    (18, 'portapacchi', 141), (18, 'manubrio', 77), (18, 'parafango', 84),
    (18, 'paracatena', 74), (18, 'pedale', 128), (39, 'copertone', 202),
    (39, 'lume', 187), (39, 'cavalletto', 79), (39, 'catena', 53),
    (39, 'selettore', 202), (39, 'pignone', 202), (39, 'manubrio', 83),
    (39, 'ruota', 110), (39, 'pedivella', 52), (19, 'pedale', 101),
    (9, 'sella', 52), (9, 'catena', 53), (9, 'deragliatore', 194),
    (9, 'lume', 152), (9, 'pignone', 140), (9, 'parafango', 97),
    (9, 'raggi', 69),
    (30, 'manopola', 156), (6, 'raggi', 61), (6, 'sella', 41),
    (25, 'manopola', 113), (18, 'ruota', 121), (18, 'manopola', 153),
    (18, 'mozzo', 75), (18, 'catena', 54), (18, 'guarnitura', 122),
    (39, 'mozzo', 65), (39, 'manopola', 139), (12, 'selettore', 147),
    (12, 'pedale', 126), (12, 'lume', 163), (12, 'manubrio', 95),
    (12, 'freno', 181), (1, 'portapacchi', 148), (1, 'parafango', 97),
    (1, 'sella', 46), (10, 'parafango', 116), (44, 'deragliatore', 167),
    (44, 'lume', 148), (44, 'guarnitura', 103), (44, 'manopola', 159),
    (44, 'bicicletta', 1818), (40, 'bicicletta', 1665), (40, 'manubrio', 88),
    (40, 'portapacchi', 163), (4, 'ruota', 125), (2, 'lume', 158),
    (2, 'parafango', 118), (2, 'cambio', 107), (2, 'catena', 40),
    (2, 'manubrio', 86), (18, 'lume', 172), (12, 'raggi', 71),
    (12, 'cavalletto', 77), (12, 'parafango', 93), (12, 'pedivella', 45),
    (12, 'deragliatore', 180), (12, 'ruota', 94), (17, 'cambio', 102),
    (17, 'catena', 46), (44, 'pedale', 128), (44, 'catena', 39),
    (46, 'raggi', 57), (46, 'manopola', 120), (46, 'paracatena', 55),
    (46, 'pedale', 124), (46, 'selettore', 204), (22, 'paracatena', 78),
    (22, 'portapacchi', 131), (22, 'raggi', 67), (22, 'pignone', 185),
    (22, 'lume', 202), (22, 'pedale', 142), (4, 'manopola', 133),
    (4, 'cavalletto', 72), (4, 'manubrio', 86), (49, 'pignone', 162),
    (49, 'disco', 119), (49, 'cavalletto', 89), (49, 'pedale', 102),
    (49, 'selettore', 171), (49, 'portapacchi', 160), (1, 'deragliatore', 153),
    (23, 'lume', 141), (23, 'pedale', 114), (23, 'cambio', 113),
    (15, 'pignone', 158), (15, 'mozzo', 65), (15, 'parafango', 108),
    (19, 'guarnitura', 92), (19, 'deragliatore', 208), (19, 'catena', 46),
    (19, 'mozzo', 79), (6, 'mozzo', 58), (6, 'cambio', 124),
    (6, 'bicicletta', 1971), (6, 'parafango', 96), (6, 'selettore', 169),
    (6, 'disco', 137), (34, 'cambio', 147), (34, 'copertone', 193),
    (5, 'pignone', 172), (5, 'paracatena', 73), (5, 'pedale', 104),
    (24, 'bicicletta', 1646), (24, 'disco', 135), (24, 'copertone', 144),
    (24, 'pedale', 137), (31, 'bicicletta', 2239), (31, 'pignone', 192),
    (31, 'cambio', 107), (31, 'catena', 54), (37, 'pignone', 152),
    (37, 'portapacchi', 166), (37, 'ruota', 112), (37, 'paracatena', 58),
    (37, 'disco', 125), (33, 'parafango', 114), (33, 'bicicletta', 1741),
    (33, 'sella', 43), (33, 'deragliatore', 176), (44, 'paracatena', 79),
    (44, 'copertone', 172), (44, 'freno', 164), (44, 'cavalletto', 84),
    (38, 'ruota', 119), (38, 'parafango', 87), (5, 'bicicletta', 1856),
    (5, 'manubrio', 87), (5, 'mozzo', 75), (34, 'mozzo', 58),
    (16, 'pedale', 103), (16, 'catena', 42), (16, 'portapacchi', 122),
    (16, 'ruota', 140), (16, 'selettore', 198), (16, 'guarnitura', 127),
    (17, 'freno', 126), (17, 'disco', 142), (17, 'ruota', 103),
    (17, 'manubrio', 73), (17, 'mozzo', 76), (11, 'mozzo', 57),
    (11, 'cambio', 124), (11, 'guarnitura', 114), (11, 'copertone', 205),
    (11, 'portapacchi', 166), (21, 'disco', 140), (21, 'bicicletta', 1741),
    (21, 'paracatena', 70), (21, 'freno', 137), (21, 'parafango', 91),
    (21, 'selettore', 213), (7, 'deragliatore', 208), (9, 'guarnitura', 96),
    (33, 'manopola', 156), (33, 'pignone', 174), (33, 'catena', 50),
    (38, 'sella', 40), (38, 'catena', 50),
    (38, 'raggi', 69), (38, 'lume', 165), (38, 'bicicletta', 2277),
    (8, 'freno', 181), (8, 'cambio', 119), (10, 'catena', 48),
    (10, 'manubrio', 71), (10, 'copertone', 191), (17, 'pedale', 101),
    (48, 'guarnitura', 103), (48, 'manopola', 147), (48, 'disco', 147),
    (48, 'ruota', 127), (48, 'manubrio', 94), (36, 'disco', 108),
    (36, 'guarnitura', 131), (36, 'pedivella', 56), (36, 'lume', 160),
    (36, 'freno', 172), (36, 'cavalletto', 80), (33, 'freno', 137),
    (33, 'portapacchi', 151), (33, 'copertone', 154), (33, 'paracatena', 67),
    (33, 'disco', 125), (33, 'mozzo', 78), (18, 'disco', 120),
    (20, 'portapacchi', 135), (20, 'manubrio', 66), (20, 'freno', 141),
    (20, 'pedivella', 44), (20, 'disco', 105), (15, 'selettore', 189),
    (15, 'freno', 141), (15, 'lume', 196), (15, 'catena', 52),
    (15, 'deragliatore', 176), (15, 'bicicletta', 2028), (25, 'lume', 199),
    (30, 'cavalletto', 90), (30, 'catena', 52), (30, 'manubrio', 72),
    (30, 'pedale', 137), (28, 'guarnitura', 116), (28, 'disco', 102),
    (28, 'deragliatore', 158), (28, 'ruota', 125), (28, 'cavalletto', 85),
    (39, 'pedale', 117), (39, 'freno', 154), (39, 'bicicletta', 1760),
    (39, 'raggi', 71), (18, 'deragliatore', 172), (18, 'pedivella', 41),
    (42, 'cavalletto', 74), (42, 'catena', 47), (42, 'raggi', 63),
    (42, 'bicicletta', 2028), (6, 'ruota', 140), (6, 'freno', 127),
    (6, 'catena', 41), (6, 'pignone', 141), (6, 'paracatena', 54),
    (33, 'guarnitura', 93), (14, 'cambio', 121), (14, 'manubrio', 74),
    (14, 'lume', 197), (14, 'raggi', 59), (14, 'cavalletto', 74),
    (37, 'raggi', 61), (12, 'paracatena', 67), (12, 'mozzo', 69),
    (12, 'manopola', 168), (12, 'catena', 43), (12, 'sella', 42),
    (41, 'bicicletta', 1646), (41, 'catena', 43), (28, 'raggi', 78),
    (28, 'pedivella', 56), (28, 'parafango', 84), (45, 'disco', 104),
    (45, 'ruota', 95), (45, 'bicicletta', 2067), (45, 'cavalletto', 74),
    (1, 'manopola', 130), (21, 'sella', 40), (34, 'portapacchi', 129),
    (34, 'raggi', 80), (34, 'freno', 147), (34, 'catena', 44),
    (34, 'pedivella', 43), (32, 'parafango', 87), (32, 'manubrio', 91),
    (32, 'cambio', 121), (32, 'mozzo', 69), (32, 'raggi', 70),
    (32, 'guarnitura', 111), (1, 'disco', 121), (1, 'bicicletta', 1569),
    (1, 'ruota', 121), (1, 'manubrio', 78), (1, 'pedivella', 42),
    (1, 'raggi', 80), (36, 'portapacchi', 146), (36, 'ruota', 109),
    (36, 'manopola', 153), (36, 'sella', 55), (36, 'selettore', 209),
    (36, 'copertone', 190), (45, 'cambio', 111), (45, 'guarnitura', 107),
    (33, 'manubrio', 71), (33, 'cavalletto', 72), (33, 'pedivella', 46),
    (47, 'paracatena', 67), (47, 'cavalletto', 66), (47, 'guarnitura', 109),
    (47, 'manubrio', 84), (47, 'sella', 44)
]

##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da editare (questo file)
# e un file dati descritto qua di seguito.
#
# - File 'cantieri.csv'
#   Il file memorizza le informazioni sulle vendite effettuate da un negozio
#   che vende biciclette o parti di bicicletta.
#   Un esempio del contenuto del file e' visibile nella stringa seguente.
#   La prima riga descrive la struttura delle righe successive.
#   Ogni riga contiene un numero variabile di informazioni.
#   I valori sono separati da ; e per andare a capo e' utilizzato il \r\n
"""
id_bici;data;pezzo;costo;...
20;01/01/2000;sella;54;pedale;134;copertone;205;bicicletta;2047;manopola;161
10;03/01/2000;cambio;113;mozzo;82;paracatena;60
47;03/01/2000;copertone;158
21;04/01/2000;portapacchi;135;cavalletto;75;catena;45
48;04/01/2000;parafango;99;pedale;122;bicicletta;1569;cambio;110
28;07/01/2000;mozzo;77;copertone;153;manopola;129;selettore;152;pedale;112;freno;141
6;07/01/2000;manopola;130;copertone;200;pedivella;42;pedale;124;guarnitura;93
44;08/01/2000;parafango;115;pedivella;58
45;08/01/2000;raggi;57;freno;140;sella;46;manopola;116
41;11/01/2000;manubrio;75;sella;52;ruota;112;selettore;156;parafango;90
16;13/01/2000;copertone;181;disco;135;cavalletto;87;parafango;110;pedivella;49;pignone;155
24;13/01/2000;portapacchi;144;manopola;159;guarnitura;103
3;16/01/2000;parafango;88;pedivella;52;bicicletta;2258;ruota;125;copertone;181
30;16/01/2000;bicicletta;1837
44;16/01/2000;sella;50
11;21/01/2000;bicicletta;2277;pedivella;49;freno;143;raggi;61;sella;54;manubrio;65

...
"""
#   In ogni record (record e' un sinonimo di 'riga')
#   sono memorizzate le informazioni seguenti.
#   - id_bici. E' un valore numerico che identifica univocamente
#     una bicicletta venduta o la bicicletta per la quale
#     è stato venduto un pezzo di ricambio. I ricambi sono sempre venduti
#     a persone che hanno acquistato o acquisteranno una bicicletta
#     nel corso dell'anno.
#     Data una bicicletta, i ricambi possono essere acquistati
#     anche prima della bicicletta stessa. I ricambi possono essere
#     acquistati in momenti diversi dell'anno (quindi possono
#     essere presenti più righe relative ad una stessa bicicletta
#     sparse per il file ).
#   - data. La data in cui sono stati venduti gli oggetti descritti nella riga (vedi elementi successivi).
#   - Dopo la data sono presenti un numero variabile di coppie "nome_oggetto" e "prezzo".
#     In ogni riga ci possono essere una o piu' coppie. Per ogni coppia sono presenti:
#     * nome_oggetto acquistato. Rappresenta il nome dell'oggetto acquistato.
#       "bicicletta" significa che e' stata acquistato una bicicletta intera,
#       altrimenti è presente il nome del pezzo di ricambio acquistato.
#     * prezzo. Indica il prezzo dell'oggetto.
#
#   Alcune note sul contenuto del file
#   - I dati sull'acquisto della bicicletta o dei pezzi di ricambio
#     possono essere sparsi su più righe non vicine tra loro.
#   - L'acquisto dei pezzi di ricambio per una bicicletta può avvenire
#     anche molto prima dell'acquisto della bicicletta stessa.
#
#   ***NOTA BENE***: aprite il file .csv
#     - con un editor di testo diverso da notepad
#     - senza usare excel (o programmi similari)

##########################################################
# INTRODUZIONE AL LAVORO DA SVOLGERE
##########################################################
#
# Implementate le seguenti funzioni, il commento che precede
# ogni funzione vi spiegherà in dettaglio che cosa fare.
# Controllate nel corpo principale del programma (in fondo
# allo script), come vengono invocate le funzioni che
# implementerete.
# Per favore NON USATE le istruzioni input() o raw_input()
# nel codice che scriverete.
# Se volete, potete implementare delle funzioni aggiuntive
# rispetto a quelle gia' presenti qua sotto.

##########################################################
# INIZIO DELLA PARTE DA EDITARE
##########################################################

cognome = 'Sostituiscimi con il cognome'  # inserisci qua il tuo cognome
nome = 'Sostituiscimi con il nome'  # inserisci qua il tuo nome

# - La funzione seguente, caricaDatiBici(), accetta come parametro in ingresso
#   il nome del file .csv contenente i dati descritti in precedenza.
#   La funzione deve leggere il contenuto del file e
#   restituire una lista di tuple, come nell'esempio seguente:
#        [
#          ('id_biciclettaA', 'nome_oggetto1', prezzo1),
#          ('id_biciclettaA', 'nome_oggetto2', prezzo2),
#          ('id_biciclettaB', 'nome_oggetto3', prezzo3),
#          ('id_biciclettaB', 'nome_oggetto4', prezzo4),
#          ...
#        ]
#   dove ogni tupla contiene le informazioni su un oggetto acquistato.
#   Per esempio, la funzione applicata ad un file con il contenuto seguente
"""
id_bici;data;pezzo;costo;...
10;03/01/2000;cambio;113;mozzo;82;paracatena;60
47;03/01/2000;copertone;158
...
"""


#   deve restituire una struttura dati come la seguente
#   [
#     (10,'cambio',113),
#     (10,'mozzo',82),
#     (10,'paracatena',60), # qui finiscono i dati della prima riga di dati del file, che fanno tutti riferimento a id_bici 10
#     (47,'copertone',158), # qui invece c'e' l'unico oggetto della seconda riga di dati del file, il copertone e' stato acquistato per id_bici 47
#     ...
#   ]
#   Ogni tupla corrisponde ad un oggetto venduto descritto nel file.
#   In ogni tupla devono essere presenti 3 valori, rispettivamente:
#   l'id_bici, il nome dell'oggetto acquistato, il prezzo dell'oggetto.
#   Tutti i valori nella tupla devono essere di tipo intero, ad eccezione
#   del nome dell'oggetto che deve essere di tipo stringa.
#   **NOTA BENE**: il risultato restituito da questa funzione e' utilizzato dalle funzioni
#   successive, se in via provvisoria volete lavorare sulle funzioni successive
#   senza implementare l'attuale, potete utilizzare la struttura dati creata
#   all'inizio di questo script togliendo il commento dalla prima riga di codice.
#   In quest'ultimo caso tuttavia la funzione sara' considerata non implementata.

def caricaDatiBici(fn):
	file=open(fn,"r")
	file.readline()
	listaTuple=[]
	for riga in file:
		records=riga.strip("\n").split(";")
		i=2
		while i+1<len(records):
			tupla=(int(records[0]), records[i], int(records[i+1]))
			i+=2
			listaTuple.append(tupla)
	listaTuple.sort(key=lambda x:x[0])
	file.close()
	return listaTuple



# - La funzione calcolaCostoMedio() accetta come parametri in ingresso
#   la struttura dati restituita dalla funzione caricaDatiBici().
#   La funzione calcolaCostoMedio() deve restituire un dizionario con indicato,
#   per ogni bici, il costo medio dei prezzi acquistati,
#   escludendo dal calcolo il costo della bicicletta (nome oggetto: "bicicletta").
#   La funzione deve restituire un dizionario come il seguente:
#   {id_bici1:costo_medio1, id_bici2:costo_medio2, id_bici3:costo_medio3, ...}
#   dove ogni chiave e' un id_bici e costo_medio e' il costo medio dei ricambi acquistati
#   per la bicicletta, escludendo il costo di acquisto della bicicletta.
#   Per esempio se la struttura dati ricevuta in ingresso fosse:
#   [
#     (10,'cambio',100),
#     (10,'mozzo',81),
#     (10,'bicicletta',1100),
#     ...
#   ]
#   la funzione dovrebbe restituire un dizionario come il seguente:
#   {10:90.5}
#   Nel calcolo della media sono stati considerati i prezzi di
#   "cambio" e "mozzo" con risultato (100+81)/2=90.5
#   Dal calcolo della media e' stato escluso il prezzo di acquisto della bicicletta.
def calcolaCostoMedio(ds):
    pass  # Implementate qua sotto il codice della funzione. La riga con il pass puo' essere cancellata.
dati=caricaDatiBici("biciclette.csv")
diz={}
prezzoTot=0
idBici=1
i=0
for n in dati:
	if idBici!=n[0]:
		if i!=0:
			diz[idBici]=round(prezzoTot/i, 2)
		else:
			diz[idBici]=prezzoTot
		prezzoTot=0
		i=0
		if n[1]!='bicicletta':
			idBici=n[0]
			prezzoTot+=n[2]
			i+=1
		elif n[1]=='bicicletta':
			idBici=n[0]
	elif idBici==n[0]:
		if n[1]!='bicicletta':
			prezzoTot+=n[2]
			i+=1

		
print(diz)

# - La funzione numeroCombinazioni() accetta come parametri in ingresso
#   la struttura dati restituita dalla funzione caricaDatiBici().
#   La funzione numeroCombinazioni() deve restituire il valore intero che corrisponde
#   al numero di biciclette per le quali sono stati venduti tutti e tre questi oggetti:
#   "sella"
#   "cambio"
#   "manubrio"
#   Se per una bicicletta non sono stati acquistati tutti e tre gli oggetti,
#   tale bicicletta va esclusa dal conteggio.
#   Tenete conto che nei dati di acquisto, il compratore non compra mai
#   lo stesso oggetto due volte per la stessa bicicletta.
#   Per esempio, se la funzione riceve in ingresso i dati seguenti
#   [
#     (10,'sella',100),
#     (10,'cambio',50),
#     (10,'manubrio',200),
#     (10,'mozzo',50),
#     (21,'copertone',80),
#     (21,'cambio',50),
#     (15,'sella',90),
#     (15,'cambio',40),
#     (15,'manubrio',150) # non ci sono altre tuple nella lista
#   ]
#   La funzione deve restituire il valore 2, perche'
#   solo per le biciclette 10 e 15 sono stati venduti "sella", "cambio" e "manubrio".
#   Nota bene:
#   - per la bicicletta 21 non sono stati venduti tutti e 3 gli oggetti cercati.
#   - la bicicletta 10 e' stata contata anche se oltre ai 3 oggetti e' stato
#     venduto un oggetto in piu' ("mozzo").
def numeroCombinazioni(dc):
    pass  # Implementate qua sotto il codice della funzione. La riga con il pass puo' essere cancellata.


# - La funzione maggiorIncasso() accetta come parametri in ingresso
#   la struttura dati restituita dalla funzione caricaDatiBici().
#   La funzione maggiorIncasso() deve restituire una tupla contente
#   il nome del pezzo che ha generato l'incasso maggiore e l'ammontare dello
#   stesso: (nomePezzo, TotaleIncassato).
#   Dalla ricerca devono essere esclusi i costi di acquisto delle biciclette
#   (nome oggetto: "bicicletta").
#   Se ci fossero piu' pezzi a pari merito, sceglietene uno con il criterio che preferite
def maggiorIncasso(dc):
    pass  # Implementate qua sotto il codice della funzione. La riga con il pass puo' essere cancellata.
"""

##########################################################
# Fine del compito e della parte da editare obbligatoriamente.
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################

print('-' * 30)
print('Esercizio %s.' % (nomeEsercizio))
print('Ciao nome: %s, cognome: %s.' % (nome, cognome))

print('1) Eseguo la funzione caricaDatiBici: ')
csvfn = 'biciclette.csv'
db = caricaDatiBici(csvfn)
print(db)

print('2) Eseguo la funzione calcolaCostoMedio: ')
res2 = calcolaCostoMedio(db)
print(res2)

print('3) Eseguo la funzione numeroCombinazioni: ')
res3 = numeroCombinazioni(db)
print(res3)

print('4) Eseguo la funzione maggiorIncasso: ')
res4 = maggiorIncasso(db)
print(res4)

print('Nome file e autore dello script eseguito')
print('Autore: %s, %s' % (nome, cognome))
print('-' * 30)
"""