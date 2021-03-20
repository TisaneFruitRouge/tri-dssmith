

function getDate()
{
	let currentDate = new Date();

	return `${currentDate.getDate()}-${currentDate.getMonth()}-${currentDate.getFullYear()}_${currentDate.getHours()}:${currentDate.getMinutes()}:${currentDate.getSeconds()}`
}

export {
	getDate
}