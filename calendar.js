<style>
#calendar4 {
  width: 100%;
  font: monospace;
  line-height: 1.2em;
  font-size: 15px;
  text-align: center;
}
#calendar4 thead tr:last-child {
  font-size: small;
  font-weight: 700;
  color: rgb(103, 103, 103);
}
#calendar4 tbody td {
  color: rgb(44, 86, 122);
}
#calendar4 tbody td:nth-child(1) {
  font-size: small;
  color: rgba(103, 103, 103, .7);
}
#calendar4 tbody td:nth-child(n+7), #calendar4 .holiday {
  color: rgb(231, 140, 92);
}
#calendar4 tbody td.today {
  outline: 3px solid red;
}
</style>

<table id="calendar4">
  <thead>
    <tr><td><td colspan="4"><select>
<option value="0"></option>
<option value="1"></option>
<option value="2"></option>
<option value="3"></option>
<option value="4"></option>
<option value="5"></option>
<option value="6"></option>
<option value="7"></option>
<option value="8"></option>
<option value="9"></option>
<option value="10"></option>
<option value="11"></option>
</select><td colspan="3"><input type="number" value="" min="0" max="9999" size="4">
    <tr><td><td><td><td><td><td><td><td>
  <tbody>
</table>

<script>
function Calendar4(id, year, month) {

Date.prototype.getWeek = function () {
    var target  = new Date(this.valueOf());
    var dayNr   = (this.getDay() + 6) % 7;
    target.setDate(target.getDate() - dayNr + 3);
    var firstThursday = target.valueOf();
    target.setMonth(0, 1);
    if (target.getDay() != 4) {
        target.setMonth(0, 1 + ((4 - target.getDay()) + 7) % 7);
    }
    return 1 + Math.ceil((firstThursday - target) / 604800000);
}

var Dlast = new Date(year,parseFloat(month)+1,0).getDate(),
    D = new Date(year,month,Dlast),
    DNlast = D.getDay(),
    DNfirst = new Date(D.getFullYear(),D.getMonth(),1).getDay(),
    m = document.querySelector('#'+id+' option[value="' + D.getMonth() + '"]'),
    g = document.querySelector('#'+id+' input');

if (new Date(D.getFullYear(),D.getMonth(),1).getWeek() < 10) {
  calendar = '<tr><td>0' + new Date(D.getFullYear(),D.getMonth(),1).getWeek();
}else{
  calendar = '<tr><td>' + new Date(D.getFullYear(),D.getMonth(),1).getWeek();
}

if (DNfirst != 0) {
  for(var  i = 1; i < DNfirst; i++) calendar += '<td>';
}else{
  for(var  i = 0; i < 6; i++) calendar += '<td>';
}

for(var  i = 1; i <= Dlast; i++) {
  if (i == new Date().getDate() && D.getFullYear() == new Date().getFullYear() && D.getMonth() == new Date().getMonth()) {
    calendar += '<td class="today">' + i;
  }else{
    if (
        (i == 1 && D.getMonth() == 0 && ((D.getFullYear() > 1897 && D.getFullYear() < 1930) || D.getFullYear() > 1947)) ||
        (i == 2 && D.getMonth() == 0 && D.getFullYear() > 1992) ||
        ((i == 3 || i == 4 || i == 5 || i == 6 || i == 8) && D.getMonth() == 0 && D.getFullYear() > 2004) ||
        (i == 7 && D.getMonth() == 0 && D.getFullYear() > 1990) ||
        (i == 23 && D.getMonth() == 1 && D.getFullYear() > 2001) ||
        (i == 8 && D.getMonth() == 2 && D.getFullYear() > 1965) ||
        (i == 1 && D.getMonth() == 4 && D.getFullYear() > 1917) ||
        (i == 9 && D.getMonth() == 4 && D.getFullYear() > 1964) ||
        (i == 12 && D.getMonth() == 5 && D.getFullYear() > 1990) ||
        (i == 7 && D.getMonth() == 10 && (D.getFullYear() > 1926 && D.getFullYear() < 2005)) ||
        (i == 8 && D.getMonth() == 10 && (D.getFullYear() > 1926 && D.getFullYear() < 1992)) ||
        (i == 4 && D.getMonth() == 10 && D.getFullYear() > 2004)
       ) {
      calendar += '<td class="holiday">' + i;
    }else{
      calendar += '<td>' + i;
    }
  }
  if (new Date(D.getFullYear(),D.getMonth(),i).getDay() == 0 && i != Dlast) {
    if (new Date(D.getFullYear(),D.getMonth(),i).getWeek() < 9) {
      calendar += '<tr><td>0' + new Date(D.getFullYear(),D.getMonth(),i+1).getWeek();
    }else{
      calendar += '<tr><td>' + new Date(D.getFullYear(),D.getMonth(),i+1).getWeek();
    }
  }
}

if (DNlast != 0) {
  for(var  i = DNlast; i < 7; i++) calendar += '<td>';
}

document.querySelector('#'+id+' tbody').innerHTML = calendar;
g.value = D.getFullYear();
m.selected = true;

if (document.querySelectorAll('#'+id+' tbody tr').length < 6) {
    document.querySelector('#'+id+' tbody').innerHTML += '<tr><td>&nbsp;<td><td><td><td><td><td><td>';
}

document.querySelector('#'+id+' option[value="' + new Date().getMonth() + '"]').style.color = 'rgb(220, 0, 0)';

}

Calendar4("calendar4",new Date().getFullYear(),new Date().getMonth());
document.querySelector('#calendar4').onchange = function Kalendar4() {
  Calendar4("calendar4",document.querySelector('#calendar4 input').value,document.querySelector('#calendar4 select').options[document.querySelector('#calendar4 select').selectedIndex].value);
}
</script>