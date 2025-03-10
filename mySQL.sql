CREATE SCHEMA biosecurity;

USE biosecurity;

CREATE TABLE IF NOT EXISTS `user`
(
user_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
username varchar(50) not null,
`password` varchar(255) not null,
user_role varchar(25) default 'mariner'
);


CREATE TABLE IF NOT EXISTS staff
(
staff_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
first_name varchar(50) not null,
last_name varchar(50) not null,
email varchar(100) not null,
work_phone varchar(15),
department varchar(50) not null,
`position` varchar(50),
hire_date date not null,
active_user tinyint default 1,
user_id int not null, 
FOREIGN KEY (user_id) REFERENCES user(user_id)
ON UPDATE CASCADE
ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS mariner
(
mariner_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
first_name varchar(50) not null,
last_name varchar(50),
email varchar(100) not null,
phone varchar(15),
address varchar(100),
date_joined date,
active_user tinyint default 1,
user_id int not null,
FOREIGN KEY (user_id) REFERENCES user(user_id)
ON UPDATE CASCADE
ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS guide
(
ocean_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
ocean_item_type enum('pest', 'disease') not null,
present_in_NZ enum('yes', 'no') not null,
common_name varchar(100) not null,
scientific_name varchar(100) not null,
`description` longtext not null,
threats longtext,
key_characteristics longtext,
location longtext
);


CREATE TABLE IF NOT EXISTS image
(
ocean_id INT NOT NULL,
image_path varchar(255) not null,
image_name varchar(100) not null,
primary_image tinyint default 0,
FOREIGN KEY (ocean_id) REFERENCES guide(ocean_id)
ON UPDATE CASCADE
ON DELETE CASCADE
);


INSERT INTO `user` (username, `password`, user_role) VALUES 
	('admin', 'd19a477e800d012db01c1e4addc1c7da8b6060b3d5aad704a196e25dbdb7a862', 'admin'),
	('staff.ellen', '5cb93d01c78ae8db0c27bea694304d95c56e7ee01e9f4b5e7f880421373696b7', 'staff'),
	('staff.will', 'a10f620eaa3ff1a1766891c8f613b142677c4ff3ce8ff38e688cf763f47e0256', 'staff'),
	('staff.vickie', 'b0db1a2ba2e62365015631eed039a4196e7cfd82d563ed67a95810c983985252', 'staff'),
	('raglan123', '62db4f91c8304e38f1b5ed1fcb03a640ebd8ebf504c8a8beba2e5ccb2afc5c03', 'mariner'),
	('bill1990', 'cfe1d7ac30d056479c2429d940d955b8c26bbea3ce13d1f4a4b7ed97e4c7bdd7', 'mariner'),
	('annie_hall', '27c85aa4a497e56f9a2fe82c81746368f9172b4f1afe27211262f771d0fe13cd', 'mariner'),
	('dave_clifton', 'c46273f449353d97acc3e830654a5da96ac2ebf049379704aed493274b7b360d', 'mariner'),
	('wiskylover99', '1a0db16b17e44768ef1ca2e8392936178db366c3b8b7d72cdb58af5b729c4825', 'mariner');
        
INSERT INTO staff (first_name, last_name, email, work_phone, department, `position`, hire_date, active_user, user_id) VALUES 
	('Green', 'Hope', 'green.hope@biosecurity.com', '0211661231', 'Editorial Team', 'Editor-in-Chief', '2023-06-01', '1', '1'),
	('Ellen', 'Waverley', 'ellen.waverley@gmail.com', '0211661232', 'Editorial Team', 'Editor', '2023-07-01', '1', '2'),
	('Will', 'Smith', 'will.smith@gmail.com', '0211661233', 'Editorial Team', 'Editor', '2023-07-01', '1', '3'),
	('Vickie', 'Wang', 'vickie_wang@gmail.com', '0211661234', 'Editorial Team', 'Editor', '2023-07-01', '1', '4');

INSERT INTO mariner (first_name, last_name, email, phone, address, date_joined, active_user, user_id) VALUES 
	('Raglan', 'Smith', 'raglan123@gmail.com', '02754365286', '26 King Street, Christchurch', '2023-08-01', '1', '5'),
	('Bill', 'Wilson', 'bill1990@hotmail.com', '033245678', '27 Hastings Street, Auckland', '2023-08-02', '1', '6'),
	('Annie', 'Hall', 'annie2000@qq.com', '0743277893', '59 George Street, Dunedin','2023-08-02', '1', '7'),
	('Dave', 'Clifton', 'dave_clifton@gmail.com', '0294458423', '37 Sunset Road, Gisborne', '2023-09-03', '1', '8'),
	('Warm', 'Bubbly', 'wiskylover99@gmail.com', '034156784', '17 Ocean Road, Nelson', '2023-09-13', '1', '9');
    
INSERT INTO guide (ocean_item_type, present_in_NZ, common_name, scientific_name, `description`, threats, key_characteristics, location) VALUES
	('pest',
	'yes',
	'Mediterranean fanworm',
	'Sabella spallanzanii',
	'The Mediterranean fanworm can persist in a range of water temperatures and salinity. It grows rapidly in summer months and can live for 2-5 years. Larvae may last in the water column for up to 20 days before settling to attach on the seafloor or on port or harbour infrastructure. The Mediterranean fanworm is spread to new locations primarily within vessel biofouling, although the movement of aquaculture equipment or other marine structures may also contribute to its spread.',
	'The Mediterranean fanworm can form dense colonies of up to 1000 individuals per square metre that will exclude the settlement of other organisms. It also has a high filtering ability that may influence the composition of planktonic communities and abundance of some species. The presence of the Mediterranean fanworm in areas where mussels or oysters are located may affect their growth due to competition for food. The tubes of the Mediterranean fanworm may attached themselves to aquaculture equipment or vessels and this may increase harvesting or fuel costs, respectively.',
	'The Mediterranean fanworm is a sessile organism that has a long leathery, flexible tube that is pale brown in colour and has a muddy appearance. These tubes normally grow to a length of 10-50 centimetres although in New Zealand individuals 80 centimetres in length have been recorded. It is larger than other native fanworms in New Zealand. The Mediterranean fanworm extends a spiral fan of yellow-orange filaments to collect plankton from the water column',
	'The Mediterranean fanworm is native to the Mediterranean and Atlantic coast of Europe. It typically occurs in subtidal habitats to a depth of 30 metres that are protected from wave exposure. The fanworm attaches to solid structures such as wharf pilings and shells or small, hard substrata in soft sediments. It has been introduced to Australia and was first detected in New Zealand in 2008. It is now present in a number of New Zealand harbours.'
	),
	('pest',
	'yes',
	'Australian droplet tunicate',
	'Eudistoma elongatum',
	'The Australian droplet tunicate is generally submerged just below the waterline, but can often be seen at low tide. The size of the Australian droplet tunicate in New Zealand is influenced by seawater temperatures, with it decreasing in size over the winter months, but rapidly re-growing to its full size once summer arrives.',
	'The Australian droplet tunicate forms dense colonies, smothering beaches, rocks and tide-pools. It displaces native species and grows on boats, aquaculture equipment and other marine structures. It was first reported in New Zealand in early 2005, but was not originally regarded as a pest, given its low density and the fact it appeared to die off in winter. In the summer of 2007-2008 it became more prolific in a number of locations in Northland and has continued to reappear over the summer months.',
	'The Australian droplet tunicate looks like clusters of white or cream coloured tubes or "sausages". Each tube or "sausage" is actually a cylinder or tunic, containing numerous small individuals. The long cylindrical heads are generally 5-30 cm long and in some instances can reach 1.5 metres and 5-20 mm in diameter.  The white tunics contain many small individual organisms and can sometimes appear orange flecked due to the presence of bright orange larvae.',
	'The Australian droplet tunicate is an ascidian native to Australia, which forms large colonies that attach to hard substrates. It is generally found in muddy bottomed tidal habitats and on man-made structures such as wharf piles and aquaculture equipment.'
	),
	('pest',
	'yes',
	'Clubbed tunicate',
	'Styela clava',
	'The clubbed tunicate is found in low energy environments such as ports and harbours and it has wide physiological tolerances. It has been found to reach high densities of 500-1500 individuals per square metre and is an efficient suspension feeder. Because of these two features it can outcompete other species for habitat and food.',
	'The clubbed tunicate can outcompete other species due to it reaching such high densities and being an efficient suspension feeder. As a fouling organism it can decrease the productivity of cultured species and increase aquaculture processing and harvesting costs. It also results in higher fuel and maintenance costs for vessels. In Japan it has caused asthmatic symptoms in individuals who shuck fouled oysters in poorly ventilated areas.',
	'The clubbed tunicate has as a long, tough, leathery skinned cylindrical form, tapering to a stalk with a disc shaped holdfast that anchors them to hard surfaces. The sea squirt ranges in colour from yellowish to reddish to brownish and can grow up to 160mm in length. Underwater it often appears fuzzy with secondary growth coating it. Under water, two short siphons or openings are visible at the top of the organism. Similar looking native New Zealand species such as Pyura pachydermatina also have a stalk, however, their stalk is much longer.',
	'The clubbed tunicate is an ascidian that grows on both natural and artificial hard marine surfaces. It is most commonly observed on wharf pilings, aquaculture structures, ropes and vessel hulls. They may also be found attached to rocks, seaweed and on shellfish.'
	),
    ('pest',
	'yes',
	'Pyura sea squirt',
	'Pyura Praeputialis',
	'Pyura praeputialis is an intertidal and shallow water species of tunicate. It is one of three species of "cunjevoi" in Australasia. It is the first reported species of marine organism to create a "foam-nest" for its larvae.',
	'Forms dense populations or mats that could displace important native species including green shell mussels.',
	'Hard sack-like body with brown or reddish-brown leathery skin. Sand and shell material or algae may be incorporated into outer skin. Flat upper surface surrounded by a ridge, and two siphons close together that project slightly above the flat surface . Adults 15 cm or more in height (max 30 cm) and approx 3–5 cm diameter. Underwater, a distinctive “cross” may be visible in siphon openings', 
	'Rocky intertidal, or rocky surfaces in the shallows. Forms a mat over rocks that is often clearly visible at low tide.'
	),
	('pest',
	'yes',
	'Asian date mussel',
	'Arcuatula senhousia',
	'Arcuatula senhousia, commonly known as the Asian date mussel, Asian mussel or bag mussel, is a small saltwater mussel. It lives entirely in the sediment and produces byssal threads that can form extensive mats on the sediment surface when densities are high. The Asian date mussel is fast growing, short lived (maximum 2 years) and can obtain densities of thousands per square metre. Populations typically fluctuate widely in abundance over time.',
	'The Asian date mussel alters benthic habitats through forming dense mats on soft sediments that can displace benthic communities. As it can obtain high densities and is a suspension feed it can limit the amount of plankton available as food for other species. Also anoxic conditions can occur in the sediment water interface due to the production and decomposition of large volumes of faeces and pseudofaeces.',
	'The Asian date mussel is differentiated from other mussels by its relatively small size and inflated shape, as well as by the greenish colour of its outer periostracal layer of its shell. The shell has zig-zag markings and iridescent radiating bands.  The shell is olive green/brown in colour and is easily crushed. It can grow as big as 3 cm in length.',
	'The Asian date mussel is native to the Pacific Ocean from Siberia to Singapore but it has spread to numerous locations around the globe incidentally by vessels (as biofouling or larvae in ballast water) and shellfish aquaculture. It inhabits the intertidal and subtidal zones to a depth of 20 metres and larvae preferentially settle on soft substrate but can settle on hard substrate.'
	),
	('pest',
	'yes',
	'Asian paddle crab',
	'Charybdis japonica',
	'Adult Asian paddle crabs can produce hundreds of thousands of offspring and it is thought that reproduction is limited to seawater temperatures of over 20°C. Larvae are relatively long-lived and can survive for three to four weeks potentially facilitating spread to new areas. Adults are also capable of swimming large distances. Human activities can assist in the spread of the Asian paddle crab, it likely entered New Zealand associated with vessels either as larvae entrained in ballast water or as hull fouling.',
	'The Asian paddle crab is aggressive and has the potential to compete with native crabs and other benthic species for habitat and food. It may consume shellfish species that are culturally and economically important and may be a nuisance species to water users as it can inflict a vicious bite when disturbed.',
	'The Asian paddle crab is a relatively large crab with paddle-like hind legs. Adults have a shell width of around 12cm with six distinct spines or spikes on each side of the eyes.  It ranges in colour from pale green through olive green, to a deep chestnut brown with purplish markings on the carapace (shell).Â  Most of the crabs found in the Waitemata Harbour tend to have yellow-orange and brown-orange markings on the shell and legs with white tips on the claws.',
	'The Asian paddle crab is a swimming crab native to South East Asia. It is normally found in the waters of Japan, Korea and Malaysia. It was first detected in New Zealand in 2000 and is presently found in the Waitamata and Whangarei harbours and Waikare Inlet in Northland. It inhabits intertidal to subtidal estuarine habitats and in New Zealand it is found on a number of different substrate types from fine muds to reefs.'
	),
	('pest',
	'yes',
	'Wakame asian kelp',
	'Undaria pinnatifida',
	'Asian kelp grows from the low intertidal area to subtidal depths of around 15 metres. It grows on any hard surface including shells, reefs, ropes, wharf piles, vessel hulls moorings and other artificial structures. It can form dense "forests" in sheltered reef areas.',
	'The impacts of Asian kelp are not well understood and are likely to vary depending on location. It can form dense stands under water, potentially resulting in competition for light and space which may lead to the exclusion or displacement of native plant and animal species. It also has the potential to become a nuisance for marine farms by increasing labour and harvesting costs due to fouling problems.',
	'The appearance of Asian kelp differs depending on its maturity. Mature plants are a brown, green or yellow colour and grow up to one to two metres.  They have a very visible midrib up the plant. They have a holdfast which anchors them, a stipe, or stem, and a sporophyll (a spiral shaped reproductive structure which produces spores) found at the base of the stipe. Juvenile Asian kelp have a holdfast and stem and an undivided blade and appear as a single leaf. The distinctive midrib starts becoming apparent once the plant grows over five centimetres. Asian kelp can look similar to the New Zealand kelp Ecklonia radiata, but it has a distinctive midrib up the middle of the blade plus the distinctive sporophyll.',
	'Asian kelp is native to Japan where it is cultivated for human consumption. It is spread mainly by fouling on vessel hulls and is present in almost all of New Zealand''s international ports and harbours ranging from Auckland down to Bluff including many offshore island. With the exception of Fiordland it is currently not known to have established on the West Coast of the South Island, or large areas of the North Island''s West Coast.'
	),
	('pest',
	'yes',
	'Exotic seaweed',
	'Caulerpa brachypus',
	'This seaweed can be spread through breaking into little pieces. This can happen, for example, by wave action or when anchors and fishing gear are moved into or through weed beds. Fragments are also carried easily on coastal currents. Pieces can get tangled in or stuck on equipment (for example, nets, dive and fishing gear, and crayfish pots). It can survive out of water for up to a week or more if it''s in a moist location (like in an anchor locker or a bunched-up fishing net).',
	'This exotic seaweed can spread rapidly and could affect native species.',
	'Caulerpa brachypus and Caulerpa parvifolia are closely related and appear identical. They have fronds up to 10 centimetres long that rise from long runners or roots known as stolons. They can be found growing below the tide line at between 2 metres and 30 metres on both hard surfaces and in sandy areas. In favourable conditions, they can spread rapidly, forming vast, dense beds or meadows.',
	'Caulerpa brachypus is exotic to New Zealand. It is native to the Indo-Pacific region, ranging from Africa to Australia, the Pacific Islands, and southern Japan. Caulerpa brachypus is considered an invasive pest in Florida, the United States, and Martinique in the Caribbean. Exotic seaweeds Caulerpa brachypus and Caulerpa parvifolia have been found in waters at Great Barrier Island (Aotea) and Great Mercury Island (Ahuahu).'
	),
	('disease',
	'yes',
	'Oyster parasite',
	'Bonamia exitiosa',
	'Bonamia exitiosa is a parasite infecting haemocytes of several oyster species and inducing physiological disorders and eventually death of the animal.',
	'The oyster parasite Bonamia exitiosa causes episodic, large-scale mass mortality of flat oysters in New Zealand''s Foveaux Strait fishery, reducing oyster populations to as little as ~9% of pre-disease stocks. Since 2000, NIWA has carried out regular surveys of the fishery for Fisheries NZ and the Bluff Oyster Management Company to determine the intensity and prevalence of infections and its effects on oyster stocks.',
	'Infection in oysters rarely results in clinical signs of disease and often the only indication of the infection is increased mortality.',
	'Infection with B. exitiosa is found in O. chilensis in the Foveaux Strait and other locations around South Island, New Zealand; in O. angasi in Australia; in O. edulis in Galicia (Spain); in the Adriatic Sea in Italy; in the Mediterranean Sea in France and in Cornwall in the United Kingdom; and in O. stentina in Tunisia.'
	),
	('disease',
	'yes',
	'Oyster disease',
	'Bonamia ostreae',
	'Bonamia ostreae is a shellfish disease caused by a parasite that infects and kills flat oysters, a taonga species with economic importance.',
	'Bonamia ostreae spreads through the movement of infected flat oysters. The parasite may be carried by other shellfish such as Pacific oysters, green lipped mussels and geoducks (a type of clam). It infects and eventually kills flat oysters (commonly known as Bluff oysters or tio). It is, however, not a food safety risk and fresh good quality Bluff oysters are safe to eat.',
	'Mildly infected oysters may appear heathy and in good condition, but heavy infections cause a loss of condition and the development of lesions. Intense infections kill the oyster. The disease can kill all ages of oysters, but older oysters appear to be more vulnerable. The complete lifecycle of B. ostreae has not been described.',
	'B. ostreae was first detected in the Marlborough Sounds in 2015 and later in Big Glory Bay, Rakiura (Stewart Island), in May 2017. B. ostreae has the potential to spread to the iconic flat oyster fishery in Foveaux Strait and other protected areas such as the Chatham Islands. The risk posed by B. ostreae is managed by a Controlled Area Notice (CAN), to restrict the movement of specified shellfish, farm equipment and craft and twice-yearly surveillance to monitor the location of the parasite.'
	),
	('disease',
	'yes',
	'Viral infection of bivalve',
	'Ostreid herpesvirus-1 microvariant',
	'OsHV-1 microvariant is the aetiological agent of a contagious viral disease of Pacific oysters, also affecting other bivalve species.',
	'In 2009, New Zealand''s pacific oyster industry was significantly affected by the presence of the Ostreid herpesvirus-1 microvariants (OsHV-1).',
	'OsHV-1 particles have been purified from Pacific oyster larvae in France (Le Deuff & Renault, 1999) and were observed by transmission electron microscopy to be enveloped icosahedral with electron dense cores and a diameter around 120 nm. The intranuclear location of the virus particles, their size and ultrastructure are characteristic of members of the Herpesvirales.',
	'OsHV-1 microvariants have been reported in Europe, Australia, New Zealand, and Asia.'
	),
	('disease',
	'yes',
	'Perkinsus olseni',
	'Perkinsus olseni',
	'Perkinsus olseni is a molluscan parasite notifiable to the World Organisation for Animal Health that is reported in several shellfish hosts in New Zealand, including the native green-lipped mussel Perna canaliculus.',
	'Overseas, high levels of infection by P. olseni have caused significant deaths in susceptible shellfish species. The presence of the parasite can also slow the growth rate of shellfish. No mass mortalities from P. olseni infection have been observed in New Zealand shellfish. Further, scallops are not thought to be particularly susceptible to P. olseni and this is borne out by the low prevalence of the parasite found in the samples. Importantly, the presence of P. olseni has no implications for human health.',
	'The protist is about 2 to 4 μm long. The zoospore has two flagella, which it uses to swim in its marine habitat. It is ingested by its mollusc host, which is often an oyster of the genus Crassostrea. It then becomes a trophozoite, which proliferates in the tissues of the host.',
	'Perkinsus olseni is established in New Zealand having been found in other shellfish species around the North Island and the top of the South Island.'
	),
	('pest',
	'no',
	'Northern pacific seastar',
	'Asterias amurensis',
	'The northern Pacific seastar is an eating machine. They prefer to eat mussels, clams, scallops, and other shellfish. But they will eat anything they can find, like dead fish and even each other.',
	'This seastar could decimate our native biodiversity. Their voracious appetites could damage the entire food chain. They could cause serious declines in our native bivalves (shellfish with 2 shells). They can settle on mussel lines and salmon cages, becoming a nuisance for our aquaculture industry.',
	'It has 5 arms, pointed, often upturned tips, yellow to orange colour, often with purple markings on top and yellow underneath, arms covered with many small, irregularly-arranged, chisel-like spines. It grows up to 24cm across but can reach 50cm. It often groups together in large numbers.',
	'The northern Pacific seastar comes from the north-western Pacific, near Russia and Japan. It has spread to parts of Australia. If present in New Zealand, this seastar could be anywhere on the coast.'
    ),
	('pest',
	'no',
	'Chinese mitten crab',
	'Eriocheir sinensis',
	'The Chinese mitten crab is native to China, the Korean Peninsula and Japan. It has been introduced to north eastern Europe, both coasts of the United States and eastern Canada. In some instances, the Chinese mitten crab may have been introduced purposely for human consumption but it is also transported as larvae in vessel ballast water or as juveniles and adults within hull fouling. The Chinese mitten crab spends most of its life in freshwater environments but migrates en mass to brackish (salty) waters to mate and reproduce. A single female can produce 250,000 to 1 million eggs brooding eggs that hatch as swimming larvae from winter through to early summer. Larval crabs develop in the plankton in coastal waters and settle as juveniles back into estuarine habitats. They then migrate upstream into freshwater environments, sometimes as far as 1500 km inland, where they grow into adults.',
	'In its introduced range, the Chinese mitten crab can reach very high densities. It has a broad diet and may compete with native species for food and habitat. The sub-adult crabs burrow extensively into river banks increasing the rate of erosion and can even cause levees to fail. The mass migrations can also be a nuisance to fishers through consuming fishing bait and fish caught in nets. The Chinese mitten crab is also be an intermediate host for the Oriental lung fluke (Paragonimus westermani) that can infect humans if they consume raw or under-cooked individuals.',
	'The Chinese mitten crab is brown-orange to greenish-brown in colour. It has a round body with four spines down each side, a distinctive notch between the eyes and legs which are normally twice as long as its body width. Adults have characteristically dense patches of hairs ("mittens") on both claws and this is how the species gets its name.',
	'Its native range is between Vladivostock (Russian Far East) and South China, including Japan and Taiwan. It has spread to Europe and North America.'
    ),
	('pest',
	'no',
	'Aquarium caulerpa',
	'Caulerpa taxifolia',
	'Caulerpa taxifolia is a marine macro-algae that is native to tropical waters of the Indian, Pacific and Atlantic oceans. A variety of C. taxifolia was bred for use in the aquarium trade and it has broader environmental tolerances than plants of the same species in the tropics. The aquarium type has established non-native populations in the Mediterranean, Southern California, USA and temperate areas of Australia. These have initially occurred through the release of aquarium plants either intentionally or accidentally. The Aquarium Caulerpa grows on a variety of substrata, usually between 2-35 metres deep. In the Mediterranean Sea it has been recorded at depths of 100 metres. The Aquarium Caulerpa is spread easily by vegetative growth of small fragments. It can establish in estuaries, harbours and sheltered coastal areas..',
	'The aquarium type is cold-tolerant, fast growing and, in natural environments, can form extensive, dense monoculture beds that occupy all of the available benthic habitat. It reduces the diversity of benthic habitats and species, which have flow-on effects for fishes and other mobile species. The weed is also easily entangled in fishing gear and boat propellers. In the Mediterranean Sea, fish that consume C. taxifolia accumulate toxins in their tissue..',
	'Caulerpa taxifolia is bright green. Its fronds are feather-like and flattened with a smooth midrib and branchlets (pinnules) growing equally spaced, either side of the midrib. The fronds grow from a horizontal runner (stolons) that is anchored by root-like structures (rhizoids) to the seafloor. Individual fronds of the aquarium type can be greater than 40 centimetres in length.',
	'It grows on many surfaces, including sandy sea floors, rocky outcroppings, mud, and human structures, like jetties, buoys, and ship ropes. This hardy alga has not been found in New Zealand.'
    ),
	('pest',
	'no',
	'Asian clam',
	'Potamocorbula amurensis',
	'The Asian clam is native to the northwest Pacific ocean, occurring in eastern Russia, Japan and China. It has only been found outside its native range in the San Francisco estuary, USA. It is a habitat generalist that can tolerate a broad range of salinities and survive in environments with low oxygen. The Asian clam occurs in sand, mud and clay sediments normally within shallow subtidal environments and intertidal mudflats. The clam is thought to have been introduced to San Francisco estuary as larvae in vessel ballast water. Some populations in San Francisco estuary appear to spawn year round and newly settled individuals are able to reproduce themselves within a few months. Individual clams can produce up to 220,000 eggs at a time.',
	'The Asian clam can occur in very high densities; over 25,000 per square metre. In some parts of San Francisco Bay estuary it makes up most of the biomass in the sediments. The Asian clam feeds on plankton and other organic material that is suspended in the water. At high densities, it can reduce the concentration of plankton in the water and its availability to other organisms. In San Francisco the clam is thought to have indirectly contributed to a dramatic decline in the catch rate of some fish species. It also filters toxins present in the water column which may lead to increased exposure of toxins to animals that consume them.',
	'The shell of the Asian clam can be yellow, tan or dirty white with brown staining. It measures up to 3 cm in length. One side of the shell is larger than the other, resulting in a distinctive "overbite". Old shells may have wrinkled edges.',
	'Most often on mixed sand and mud substrates. Clams are partially buried in soft material with ½ to of shell exposed above the surface. Mostly subtidal, but also intertidal. Can live in almost freshwater upper estuarine creek areas through to fully marine habitats. Subtropical to cold temperate waters.'
    ),    
	('disease',
	'no',
	'Infectious salmon anaemia',
	'Infectious salmon anaemia virus',
	'The virus is part of the influenza family of viruses. It can be carried in Atlantic salmon, rainbow trout, and sea trout. Only Atlantic salmon are known to develop the disease. In severe cases, it can kill up to 90% of farmed Atlantic salmon over 3 months.',
	'This disease has severely reduced Atlantic salmon aquaculture production. The main species of salmon farmed in New Zealand is Chinook salmon. Although evidence of its effect on Chinook salmon is limited, we do not want to have to find out the hard way. As with many viral diseases of fish, there is no specific treatment or cure. Once established, aquatic diseases are extremely difficult to eradicate.',
	'Diagnosing fish diseases requires laboratory testing. Signs of fish diseases are difficult to tell apart. In a fish farm, watch for salmon or trout that are: (1)congregating and gasping near the surface, (2)lethargic, (3)not eating, (4)progressively dying.',
	'Currently the virus is in the major Atlantic salmon growing areas. It is found in Norway, Canada, USA, Chile, UK, and the Faroe Islands. An outbreak is most likely in farmed fish in the marine environment.'
	),
	('disease',
	'no',
	'Infectious pancreatic necrosis',
	'Infectious pancreatic necrosis virus',
	'Infectious pancreatic necrosis (IPN) is a disease of freshwater and saltwater finfish. A virus causes the disease. Fish catch the virus from other fish, including their parents.',
	'IPN virus can infect a range of fish species. Keeping it out of New Zealand is particularly important for aquaculture and fisheries species. If it were found here, it could result in mass fish deaths and create barriers for our exports. IPN virus is highly contagious. If fish survive an infection, we assume they become healthy-looking carriers. Carrier fish could spread the disease to healthy fish. Once established, aquatic diseases are extremely difficult to eradicate.',
	'In farms, disease signs appear suddenly. The main sign is an unusual number of deaths in fry or fingerlings (young fish). Fish deaths may be seen as fish go from fresh water to sea water (smolts). Diagnosing fish diseases requires laboratory testing. Signs of fish diseases are difficult to tell apart. Not all infected fish show signs of disease.',
	'This disease can infect fish in both the marine and freshwater environments.'
	),
	('disease',
	'no',
	'Marteiliosis',
	'Marteilia maurini, M. refringens, M. sydneyi',
	'Marteiliosis is a disease of shellfish. Mostly it infects rock oysters, but it can also infect mussels.',
	'This disease can kill nearly all oysters it infects. If it came to New Zealand, it could devastate our oyster populations.',
	'This disease looks like many other shellfish diseases.',
	'Marteiliosis can infect a range of bivalve species but is most likely to infect oysters.'
	),
	('disease',
	'no',
	'Viral haemorrhagic septicaemia',
	'Viral haemorrhagic septicaemia virus',
	'This virus infects a broad range of wild and farmed freshwater and marine species, including rainbow trout, turbot, and Japanese flounder. It can infect fish at all life stages, but particularly young fish. Depending on the version of the virus, it can kill up to 80% of a fish population. If a fish survives, it can become a carrier and pass it on to healthy fish.',
	'Due to the huge range of species this virus can infect, some New Zealand species are likely to be susceptible. In Europe, the virus is considered one of the most serious viral diseases in trout aquaculture. As with many viral diseases of fish, there is no specific treatment or cure. Once established, aquatic diseases are extremely difficult to eradicate.',
	'Diagnosing fish diseases requires laboratory testing. Signs of fish diseases are difficult to tell apart. This virus may show different signs in different fish species. Also, infected survivors can show no signs of the disease, they are covert carriers.',
	'Infected fish could be in fresh water or the marine environment, in both farmed or wild populations.'
	);


INSERT INTO image (ocean_id, image_path, image_name, primary_image) VALUES
	('1', '/static/img/Mediterranean fanworm 1.jpg', 'Mediterranean fanworm 1', '1'),
	('1', '/static/img/Mediterranean fanworm 2.jpg', 'Mediterranean fanworm 2', '0'),
	('1', '/static/img/Mediterranean fanworm 3.jpg', 'Mediterranean fanworm 3', '0'),
	('2', '/static/img/Australian droplet tunicate 1.jpg', 'Australian droplet tunicate 1', '1'),
	('2', '/static/img/Australian droplet tunicate 2.jpg', 'Australian droplet tunicate 2', '0'),
	('2', '/static/img/Australian droplet tunicate.jpg', 'Australian droplet tunicate 3','0'),
	('3', '/static/img/Clubbed Tunicate 1.jpg', 'Clubbed Tunicate 1', '1'),
	('3', '/static/img/Clubbed Tunicate 2.jpg', 'Clubbed Tunicate 2','0'),
	('3', '/static/img/Clubbed Tunicate 3.jpg', 'Clubbed Tunicate 3','0'),
	('4', '/static/img/Pyura sea squirt 1.jpg', 'Pyura sea squirt 1', '1'),
	('4', '/static/img/Pyura sea squirt 2.jpg', 'Pyura sea squirt 2', '0'),
	('4', '/static/img/Pyura sea squirt 3.jpg', 'Pyura sea squirt 3', '0'),
	('5', '/static/img/Asian date mussel 1.jpg', 'Asian date mussel 1', '1'),
	('5', '/static/img/Asian date mussel 2.jpg', 'Asian date mussel 2', '0'),
	('5', '/static/img/Asian date mussel 3.jpg', 'Asian date mussel 3', '0'),
	('6', '/static/img/Asian paddle crab 1.jpg', 'Asian paddle crab 1',  '1'),
	('6', '/static/img/Asian paddle crab 2.jpg', 'Asian paddle crab 2', '0'),	
	('6', '/static/img/Asian paddle crab 3.jpg', 'Asian paddle crab 3', '0'),
	('7', '/static/img/Asian kelp 1.jpg', 'Asian kelp 1', '1'),
	('7', '/static/img/Asian kelp 2.jpg', 'Asian kelp 2', '0'),
	('7', '/static/img/Asian kelp 3.jpg', 'Asian kelp 3', '0'),     
	('8', '/static/img/Caulerpa brachypus 1.jpg', 'Caulerpa brachypus 1', '1'),
    ('8', '/static/img/Caulerpa 2.jpg', 'Caulerpa 2', '0'),
    ('8', '/static/img/Caulerpa beachcast at Great Barrier Island.jpg', 'Caulerpa beachcast at Great Barrier Island','0'),     
	('9', '/static/img/Bonamia exitiosa 1.jpg', 'Bonamia exitiosa 1', '1'),
	('9', '/static/img/Bonamia exitiosa 2.png', 'Bonamia exitiosa 2','0'),    
	('10', '/static/img/Bonamia ostreae 1.jpg', 'Bonamia ostreae 1', '1'),
    ('10', '/static/img/Bonamia ostreae 2.jpg', 'Bonamia ostreae 2','0'),    
	('11', '/static/img/Pacific oysters infected with OsHV-1.jpg', 'Pacific oysters infected with OsHV-1', '1'),
    ('11', '/static/img/herpes virus threatens oysters.jpg', 'herpes virus threatens oysters', '0'),    
	('12', '/static/img/Abalone infected with Perkinsus.jpg', 'Abalone infected with Perkinsus', '1'),
    ('12', '/static/img/Perkinsus olseni 1.jpg', 'Perkinsus olseni 1', '0'),
	('13', '/static/img/Northern Pacific Sea Star 1.png', 'Northern Pacific Sea Star 1', '1'),
	('13', '/static/img/Northern Pacific Sea Star 2.jpg', 'Northern Pacific Sea Star 2', '0'),
	('13', '/static/img/A yellow colour variant of the Northern Pacific sea star.png', 'A yellow colour variant of the Northern Pacific sea star', '0'),
	('14', '/static/img/Chinese mitten crab 1.png', 'Chinese mitten crab 1', '1'),
	('14', '/static/img/Chinese mitten crab 2.jpg', 'Chinese mitten crab 2', '0'),
	('14', '/static/img/Chinese mitten crab 3.jpg', 'Chinese mitten crab 3', '0'),            
	('15', '/static/img/Aquarium Caulerpa 1.png', 'Aquarium Caulerpa 1', '1'),
	('15', '/static/img/Aquarium Caulerpa 2.png', 'Aquarium Caulerpa 2', '0'),
	('15', '/static/img/Aquarium Caulerpa 3.png', 'Aquarium Caulerpa 3', '0'),            
	('16', '/static/img/Asian clam 1.png', 'Asian clam 1', '1'),
	('16', '/static/img/Asian clam 2.png', 'Asian clam 2', '0'),            
	('17', '/static/img/Infectious salmon anemia 1.jpg', 'Infectious salmon anemia 1', '1'),
	('17', '/static/img/Infectious salmon anemia 2.jpg', 'Infectious salmon anemia 2','0'),   
	('18', '/static/img/Infectious pancreatic necrosis signs of disease.jpg', 'Infectious pancreatic necrosis signs of disease', '1'), 
	('18', '/static/img/Infectious Pancreatic Necrosis 1.jpg', 'Infectious Pancreatic Necrosis 1', '0'),           
	('19', '/static/img/Marteiliosis 1.jpg', 'Marteiliosis 1', '1'),
	('19', '/static/img/Marteiliosis 2.jpg', 'Marteiliosis 2', '0'),            
	('20', '/static/img/Viral haemorrhagic septicaemia 1.jpg', 'Viral haemorrhagic septicaemia 1', '1'),
	('20', '/static/img/Viral haemorrhagic septicaemia 2.jpg', 'Viral haemorrhagic septicaemia 2' ,'0');    