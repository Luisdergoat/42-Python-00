# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lunsold <lunsold@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/13 17:12:16 by lunsold           #+#    #+#              #
#    Updated: 2026/01/13 17:54:18 by lunsold          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(current, days):
	if(current > days):
		print("Harvest time!")
		return
	else:
		print(f"Day {current}")
	ft_count_harvest_recursive(current + 1, days)
	pass

