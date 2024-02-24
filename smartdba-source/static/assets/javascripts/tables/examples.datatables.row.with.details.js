
(function( $ ) {

	'use strict';

	var dataSearchInit = function() {
		var $table = $('#datatable-details-databaselist');

		// format function for row details
		var fnFormatDetails = function( datatable, tr ) {
			var data = datatable.fnGetData( tr );

			return [
				'<table class="table mb-none">',
					'<tr>',
						'<td><label class="mb-none text-muted"><b>&#9679; DBMS버전</b></label></td>',
						'<td><label class="mb-none text-muted">' + data[1] + '</label></td>',
					'</tr>',
					'<tr>',
						'<td><label class="mb-none text-muted"><b>&#9679; DB노드번호</b></label></td>',
						'<td><label class="mb-none text-muted">' + data[2] + '</label></td>',
					'</tr>',
					'<tr>',
						'<td><label class="mb-none text-muted"><b>&#9679; TNS정보</b></label></td>',
						'<td><label class="mb-none text-muted">' + data[3] + '</label></td>',
					'</tr>',
				'</div>'
			].join('');
		};

		// insert the expand/collapse column
		var th = document.createElement( 'th' );
		var td = document.createElement( 'td' );
		td.innerHTML = '<i data-toggle class="fa fa-plus-square-o text-mute h5 m-none" style="cursor: pointer;"></i>';
		td.className = "text-center";


		$table
			.find( 'thead tr' ).each(function() {
				this.insertBefore( th, this.childNodes[0] );
			});

		$table
			.find( 'tbody tr' ).each(function() {
				this.insertBefore(  td.cloneNode( true ), this.childNodes[0] );
			});

		// initialize
		var datatable = $table.dataTable({
			"columnDefs": [ {
			    "searchable": false,
			    "orderable": false,
			    "targets": 0
			} ],
			"order": [[ 4, 'desc' ],[ 5, 'asc' ]],
			"iDisplayLength": -1,
			"aLengthMenu": [[5, 10, 25, 50, -1], [5, 10, 25, 50, "All"]]
			// "pageLength": 150	
			// aoColumnDefs: [{
			// 	bSortable: false,
			// 	aTargets: [ 0 ],
			// 	bpageLength:50
			// }],
			// aaSorting: [
			// 	[1, 'asc']
			// ]
		});

		

		// add a listener
		$table.on('click', 'i[data-toggle]', function() {
			var $this = $(this),
				tr = $(this).closest( 'tr' ).get(0);

			if ( datatable.fnIsOpen(tr) ) {
				$this.removeClass( 'fa-minus-square-o' ).addClass( 'fa-plus-square-o' );
				datatable.fnClose( tr );
			} else {
				$this.removeClass( 'fa-plus-square-o' ).addClass( 'fa-minus-square-o' );
				datatable.fnOpen( tr, fnFormatDetails( datatable, tr), 'details' );
			}
		});
		

		

	};

	var datatableInit = function() {
		var $table = $('#datatable-details-tableList');

		// format function for row details
		var fnFormatDetails = function( datatable, tr ) {
			var data = datatable.fnGetData( tr );

			return [
				'<table class="table mb-none">',
					'<tr class="b-top-none">',
						'<td style="width:15%"><label class="mb-none text-muted"><b>&#9679; 생성일</b></label></td>',
						// '<td>' + data[6]+ ' ' + data[4] + '</td>',
						'<td><label class="mb-none text-muted">' + data[6] + '</label></td>',
					'</tr>',
					'<tr>',
						'<td><label class="mb-none text-muted"><b>&#9679; 수정일</b></label></td>',
						'<td><label class="mb-none text-muted">' + data[7] + '</label></td>',
					'</tr>',
					'<tr>',
						'<td><label class="mb-none text-muted"><b>&#9679; 사이즈</b></label></td>',
						'<td><label class="mb-none text-muted">' + data[8] + ' (MB) </label></td>',
					'</tr>',
					'<tr>',
						'<td><label class="mb-none text-muted"><b>&#9679; IT/개발담당자</b></label></td>',
						'<td><label class="mb-none text-muted">' + data[5] + ' / ' + data[9] +'('+data[11]+')'+ '</label></td>',
					'</tr>',
					'<tr>',
						'<td><label class="mb-none text-muted"><b>&#9679; 설명</b></label></td>',
						'<td><label class="mb-none text-muted">...</label></td>',
					'</tr>',
				'</div>'
			].join('');
		};

		// insert the expand/collapse column
		var th = document.createElement( 'th' );
		var td = document.createElement( 'td' );
		td.innerHTML = '<i data-toggle class="fa fa-plus-square-o text-mute h5 m-none" style="cursor: pointer;"></i>';
		td.className = "text-center";


		$table
			.find( 'thead tr' ).each(function() {
				this.insertBefore( th, this.childNodes[0] );
			});

		$table
			.find( 'tbody tr' ).each(function() {
				this.insertBefore(  td.cloneNode( true ), this.childNodes[0] );
			});

		// initialize
		var datatable = $table.dataTable({
			aoColumnDefs: [{
				bSortable: false,
				aTargets: [ 0 ]
			}],
			aaSorting: [
				[1, 'asc']
			]
		});

		// add a listener
		$table.on('click', 'i[data-toggle]', function() {
			var $this = $(this),
				tr = $(this).closest( 'tr' ).get(0);

			if ( datatable.fnIsOpen(tr) ) {
				$this.removeClass( 'fa-minus-square-o' ).addClass( 'fa-plus-square-o' );
				datatable.fnClose( tr );
			} else {
				$this.removeClass( 'fa-plus-square-o' ).addClass( 'fa-minus-square-o' );
				datatable.fnOpen( tr, fnFormatDetails( datatable, tr), 'details' );
			}
		});
	};

	$(function() {
		datatableInit();
		dataSearchInit();
	});

}).apply( this, [ jQuery ]);