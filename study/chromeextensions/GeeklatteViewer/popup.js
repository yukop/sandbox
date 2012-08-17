
function getImageDataListFromJSON(json) {
	var imageDataList = [];
	for (var i = 0, l = json.feed.entry.length; i < l; i = i + 3) {
		var thisTitle = json.feed.entry[i].content.$t;
		var thisImageURL = json.feed.entry[i + 1].content.$t;
		var thisEntryURL = json.feed.entry[i + 2].content.$t;
		var imageData = {
			title: thisTitle,
			imageURL: thisImageURL,
			entryURL: thisEntryURL
		};
		imageDataList.push(imageData);
	}
	return imageDataList;
}

function setImageList(anImageList) {
	$('.entryImage').attr('src', anImageList[0].imageURL);
	$('.entryUrl').attr('href', anImageList[0].entryURL); 
}

var URL = 'https://spreadsheets.google.com/feeds/cells/0Ak1KvWLO65McdGtaMC05dGh5andQWHpiNHpLX1VxZnc/od6/public/basic?alt=json'

function mainAfterGetJson(data) {
	var imageList = getImageDataListFromJSON(data);
	setImageList(imageList);
}

function main() {
	$.getJSON(URL, mainAfterGetJson);	
}

main();