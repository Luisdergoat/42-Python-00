# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lunsold <lunsold@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/13 16:52:57 by lunsold           #+#    #+#              #
#    Updated: 2026/01/13 17:54:22 by lunsold          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
	days = int(input("Days until harvest: "))
	for counter in range(1, days + 2):
		if(counter > days):
			print("Harvest time!")
		else:
			print(f"Day {counter}")
	pass
