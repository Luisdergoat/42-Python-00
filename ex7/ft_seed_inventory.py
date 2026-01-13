# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lunsold <lunsold@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/13 17:31:24 by lunsold           #+#    #+#              #
#    Updated: 2026/01/13 17:54:02 by lunsold          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed, amount, type):
	test = 0
	if(type == "packets"):
		end_type = "packets available"
		test = 1
	if(type == "grams"):
		end_type = "grams total"
		test = 2
	if(type == "area"):
		end_type = "square meters"
		test = 3
	if(test == 0):
		print("Unknown unit type")
		return
	if(end_type == "square meters"):
		print(f"{seed.capitalize()} seeds: covers {amount} {end_type}")
		return
	print(f"{seed.capitalize()} seeds: {amount} {end_type}")
	pass
