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

test('incrementProjects', function() {
    // First call should increment project once.
    result = incrementProjects(); 
    ok(result === 1, 'First call was successful'); 
    
    // Second call should increment project again. 
    result = incrementProjects(); 
    ok(result === 2, 'Second call was successful'); 
    
    result = incrementProjects(); 
    ok(result === 3, 'Third call was successful'); 
    })