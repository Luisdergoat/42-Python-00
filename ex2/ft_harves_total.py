# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harves_total.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lunsold <lunsold@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/13 16:36:05 by lunsold           #+#    #+#              #
#    Updated: 2026/01/13 17:54:36 by lunsold          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	day1 = int(input("Day 1 harvest: "))
	day2 = int(input("Day 2 harvest: "))
	day3 = int(input("Day 3 harvest: "))
	total_harvest = day1 + day2
	total_harvest = total_harvest + day3
	print(f"Total harvest: {total_harvest}")
	pass
