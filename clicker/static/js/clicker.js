/*

Openclicker -1.0 | an open source clicker game.
Copyright (C) 2013  Cheryl Yang and Ryan Lam
Contact: cheriexryan@hellokitty.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

*/

// This variable represents the current number of projects the player has made.
projects = 0; 

// This function will increment projects by 1 and update the page to reflect this change.
// Returns project for testing.
function incrementProjects() {
    projects++; 
    countDiv = document.getElementById('count'); 
    countDiv.innerHTML = projects+" open source projects made!"
    return projects; 
}