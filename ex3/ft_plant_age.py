# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lunsold <lunsold@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/13 16:44:03 by lunsold           #+#    #+#              #
#    Updated: 2026/01/13 17:54:32 by lunsold          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
	age = int(input("Enter plant age in days: "))
	if(age > 60):
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")
	pass
