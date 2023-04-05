markers = [
    (82.11244395876318, 24.017187865322565, '-4000', '-4000'),
    (67.30515645040853, 22.400875278633578, '-3000', '-3000'), #Elamite Kingdom / Invention of writing
    (52.94041247000641, 19.511255848758573, '-2000', '-2000'),
    (39.101991212026405, 15.559949833427346, '-1000', '-1000'),
    (25.76407698927707, 10.805399597802593, '1', '1'),
    (12.811563024834374, 5.532548754217401, '1000', '1000'),
    (0.0008021574031798603, 0.00042504742866794306, '2000', '2000')]

years = [i[-1][1:]+' BC' if ('-' in i[-1]) else i[-1]+' AD' for i in markers]

#(33.161615897177576, 13.544914103494255, '-559', '-559') #Kingdom of Cyrus the Great
#(17.499042382107994, 7.496435624803013, '636', '636') #Muslim invasion

ra_cyrus, dec_cyrus = 33.161615897177576, 13.544914103494255
ra_muslim, dec_muslim = 17.499042382107994, 7.496435624803013

ra_ald, dec_ald = 68.9801627900154, 16.5093023507718
ra_ple, dec_ple = 56.60099999999999, 24.114

dc_const = {
    'Ari': [(8832, 8903), (8903, 9884), (9884, 13209)],
    'Ori': [(27989, 26727), (26727, 27366), (27366, 26727), (26727, 26311),
            (26311, 25930), (25930, 25336), (25336, 25930), (25930, 25281),
            (25281, 24436), (27989, 25336), (25336, 26207), (26207, 26207),
            (26207, 27989), (23607, 22957), (22957, 22845), (22845, 22509),
            (22509, 22449), (22449, 25336), (25336, 22449), (22449, 22549),
            (22549, 22797), (22797, 23123), (27989, 28614), (28614, 29038),
            (29426, 28716), (28716, 27913), (27913, 29038)],
    'Psc': [(5742, 6193), (6193, 5586), (5586, 5742), (5742, 7097),
            (7097, 8198), (8198, 9487), (9487, 7884), (7884, 4906),
            (4906, 3786), (3786, 118268), (118268, 116771), (116771, 115830),
            (115830, 114971), (114971, 115738), (115738, 116928),
            (116928, 116771)],
    'Tau': [(26451, 21421), (21421, 20894), (20894, 20205), (20205, 20455),
            (20455, 20889), (20889, 25428), (16083, 18907), (15900, 16852),
            (20205, 18724), (18724, 16083)]
    }